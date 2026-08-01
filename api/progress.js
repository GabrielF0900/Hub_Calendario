import { Redis } from '@upstash/redis';

// Inicializa o Redis com as variáveis de ambiente geradas pela Vercel/Upstash
const redis = new Redis({
  url: process.env.KV_REST_API_URL,
  token: process.env.KV_REST_API_TOKEN,
});

export default async function handler(req, res) {
  // Configuração de CORS para permitir chamadas do front-end
  res.setHeader('Access-Control-Allow-Credentials', true);
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET,OPTIONS,PATCH,DELETE,POST,PUT');
  res.setHeader(
    'Access-Control-Allow-Headers',
    'X-CSRF-Token, X-Requested-With, Accept, Accept-Version, Content-Length, Content-MD5, Content-Type, Date, X-Api-Version, x-hub-token'
  );

  // Tratamento do preflight do CORS
  if (req.method === 'OPTIONS') {
    res.status(200).end();
    return;
  }

  if (req.method === 'GET') {
    try {
      const data = await redis.get('hubGabrielV3_progress');
      return res.status(200).json(data || {});
    } catch (error) {
      console.error('KV GET Error:', error);
      return res.status(500).json({ error: 'Erro ao buscar dados na nuvem.' });
    }
  }

  if (req.method === 'POST') {
    const token = req.headers['x-hub-token'];
    const expectedToken = process.env.PROGRESS_SYNC_TOKEN;

    if (!expectedToken) {
      console.error('PROGRESS_SYNC_TOKEN não está configurado na Vercel.');
      return res.status(500).json({ error: 'Erro de configuração do servidor.' });
    }

    if (token !== expectedToken) {
      return res.status(401).json({ error: 'Não autorizado. Token inválido.' });
    }

    try {
      const data = req.body;
      // Salva o JSON no KV Storage
      await redis.set('hubGabrielV3_progress', data);
      return res.status(200).json({ success: true, message: 'Salvo com sucesso na nuvem.' });
    } catch (error) {
      console.error('KV POST Error:', error);
      return res.status(500).json({ error: 'Erro ao salvar dados na nuvem.' });
    }
  }

  return res.status(405).json({ error: 'Método não permitido.' });
}
