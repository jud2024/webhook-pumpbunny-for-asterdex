from flask import Flask, request
import requests

app = Flask(__name__)

ASTERDEX_API_URL = 'https://api.asterdex.com/v1/order'
API_KEY = 'sua_api_key_aqui'

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    if data['action'] == 'buy':
        order = {
            'symbol': data['symbol'],
            'quantity': data['quantity'],
            'side': 'buy',
            'type': 'market',
            'apiKey': API_KEY
        }
        response = requests.post(ASTERDEX_API_URL, json=order)
        return response.json(), response.status_code
    return {'error': 'Ação não reconhecida'}, 400

if __name__ == '__main__':
    app.run(debug=True)
