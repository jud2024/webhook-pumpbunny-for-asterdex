export async function handler(event) {
  // Processa o request — ex: event.body, event.rawQueryString
  return {
    statusCode: 200,
    body: JSON.stringify({ msg: "Funfa total!" }),
  };
}
