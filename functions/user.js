// functions/user.js
export async function handler(event, context) {
  if (event.httpMethod === 'GET') {
    const userId = event.queryStringParameters.id;

    if (userId === '102220120809') {
      return {
        statusCode: 200,
        body: JSON.stringify({ id: '102220120809', name: 'Judson' }),
      };
    } else {
      return {
        statusCode: 404,
        body: JSON.stringify({ error: 'Usuário não encontrado' }),
      };
    }
  }

  return {
    statusCode: 405,
    body: JSON.stringify({ error: 'Método não permitido' }),
  };
}
