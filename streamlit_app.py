# app.py
import streamlit as st
import threading
import time
import json
from websocket import create_connection, WebSocketConnectionClosedException
import pandas as pd
import plotly.graph_objects as go
from collections import deque
import ta  # biblioteca pra indicadores técnicos
from streamlit.runtime.scriptrunner import add_script_run_ctx

# CONFIG
WS_BASE = "wss://fstream.asterdex.com/stream?streams=btcusdt@aggTrade"
SYMBOL = "btcusdt"
CANDLE_TICKS = 10
SUBSCRIBE_MSG = {"method": "SUBSCRIBE", "params": [f"{SYMBOL}@aggTrade"], "id": 1}

trade_buffer = deque(maxlen=1000)
candles = []
lock = threading.Lock()
running = True

st.set_page_config(page_title="Aster T10 Candles + RSI — BTC/USDT", layout="wide")
st.markdown("""
<style>
.corner-box {
    position: fixed; top: 12px; right: 12px;
    background: rgba(0,0,0,0.6); color: white;
    padding: 10px 14px; border-radius: 8px;
    z-index: 9999; font-family: 'Inter', sans-serif;
}
</style>
<div class="corner-box">
  <div style="font-weight:700; font-size:16px;">BTC/USDT</div>
  <div style="font-size:12px; opacity:0.9;">Timeframe: <strong>T10</strong> (10 ticks)</div>
</div>
""", unsafe_allow_html=True)

st.title("📈 Candlestick OHLC + RSI — T10 (Aster)")
placeholder_chart = st.empty()
col1, col2 = st.columns([3, 1])

with col2:
    st.subheader("Status")
    ws_status = st.empty()
    st.write("Últimos trades (até 10):")
    trades_table = st.empty()

def agg_trades_to_candles():
    global trade_buffer, candles
    with lock:
        trades = list(trade_buffer)
        n_blocks = len(trades) // CANDLE_TICKS
        new_candles = []
        for b in range(n_blocks):
            block = trades[b * CANDLE_TICKS:(b + 1) * CANDLE_TICKS]
            prices = [float(t["p"]) for t in block]
            qtys = [float(t["q"]) for t in block]
            candle = {
                "t_open": pd.to_datetime(int(block[0]["T"]), unit='ms'),
                "open": prices[0], "high": max(prices),
                "low": min(prices), "close": prices[-1],
                "volume": sum(qtys)
            }
            new_candles.append(candle)
        if n_blocks:
            for _ in range(n_blocks * CANDLE_TICKS):
                trade_buffer.popleft()
            candles.extend(new_candles)
            candles = candles[-200:]

def ws_worker():
    global running
    backoff = 1
    while running:
        try:
            ws_status.text("Conectando ao WS...")
            ws = create_connection(f"{WS_BASE}/ws")
            ws.send(json.dumps(SUBSCRIBE_MSG))
            ws_status.text("Conectado — subscribed em " + f"{SYMBOL}@aggTrade")
            backoff = 1
            while running:
                msg = ws.recv()
                if not msg: continue
                data = json.loads(msg)
                payload = data.get("data", data)
                if payload.get("e") == "aggTrade":
                    trade = {"p": payload["p"], "q": payload["q"], "T": payload["T"]}
                    with lock:
                        trade_buffer.append(trade)
        except (WebSocketConnectionClosedException, ConnectionRefusedError, OSError) as e:
            ws_status.text(f"WS desconectado — reconecta em {backoff}s (erro: {e})")
            time.sleep(backoff)
            backoff = min(30, backoff * 2)
        except Exception as ex:
            ws_status.text(f"Erro WS: {ex}")
            time.sleep(3)

# Criação da thread com contexto de execução
thread = threading.Thread(target=ws_worker, daemon=True)
add_script_run_ctx(thread)
thread.start()

try:
    while True:
        agg_trades_to_candles()
        with lock:
            df = pd.DataFrame(candles)
        if not df.empty:
            df['RSI'] = ta.momentum.rsi(df['close'], window=14, fillna=True)
            fig = go.Figure()
            fig.add_trace(go.Candlestick(
                x=df["t_open"], open=df["open"], high=df["high"],
                low=df["low"], close=df["close"], name="Candlestick"
            ))
            fig.update_layout(xaxis_rangeslider_visible=False, margin=dict(l=10, r=10, t=30, b=10),
                              template="plotly_white", height=600)

            fig_rsi = go.Figure()
            fig_rsi.add_trace(go.Scatter(x=df["t_open"], y=df["RSI"], name="RSI", line=dict(color="blue")))
            fig_rsi.add_hline(y=70, line_dash='dash', line_color="red", annotation_text="Overbought 70")
            fig_rsi.add_hline(y=30, line_dash='dash', line_color="green", annotation_text="Oversold 30")
            fig_rsi.update_layout(margin=dict(l=10, r=10, t=10, b=10), height=200, template="plotly_white")

            placeholder_chart.plotly_chart(fig, use_container_width=True)
            placeholder_chart.plotly_chart(fig_rsi, use_container_width=True)
        else:
            placeholder_chart.info("Aguardando candles... espera aí")

        with lock:
            recent_trades = list(trade_buffer)[-10:][::-1]
        if recent_trades:
            df_tr = pd.DataFrame(recent_trades)
            df_tr["price"] = df_tr["p"].astype(float)
            df_tr["qty"] = df_tr["q"].astype(float)
            df_tr["time"] = pd.to_datetime(df_tr["T"], unit='ms')
            trades_table.dataframe(df_tr[["time", "price", "qty"]])
        else:
            trades_table.write("Sem trades ainda")

        time.sleep(1)
except KeyboardInterrupt:
    running = False
    st.write("Fechando... Até mais!")
except Exception as e:
    running = False
    st.error(f"Erro “{e}” no app")
