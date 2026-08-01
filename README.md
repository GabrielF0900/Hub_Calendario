# Hub Calendário

## Configuração de Sincronização em Nuvem (Upstash Redis)

Para que o progresso seja salvo na nuvem e você possa visualizar pelo celular, é necessário seguir os passos abaixo no painel da Vercel:

### 1. Criar o Banco de Dados (Upstash for Redis)
1. Acesse o [Dashboard da Vercel](https://vercel.com/dashboard) e entre no seu projeto (`hub-calendario-coral`).
2. Vá até a aba **Storage** no menu superior.
3. Na lista de Providers, selecione a categoria **Upstash** e depois clique na opção **Upstash for Redis**.
4. Siga as instruções para criar o banco de dados Redis (aceite os termos se for a primeira vez e crie numa região padrão, como Washington D.C. - `iad1`).
5. Depois de criado, verifique se ele está conectado ao seu projeto. Isso fará com que as variáveis de ambiente necessárias (como `UPSTASH_REDIS_REST_URL` e `UPSTASH_REDIS_REST_TOKEN`) sejam preenchidas automaticamente.

### 2. Configurar o Token de Segurança
Para garantir que ninguém altere o seu progresso publicamente, a gravação é protegida por um Token que definiremos agora:
1. No seu projeto da Vercel, vá para a aba **Settings**.
2. Clique em **Environment Variables** no menu lateral esquerdo.
3. Adicione uma nova variável com os seguintes dados:
   - **Key**: `PROGRESS_SYNC_TOKEN`
   - **Value**: `CrieUmTokenSeguroAqui123` (Invente uma senha ou texto aleatório e guarde-o)
4. Clique em **Save**.
5. Como adicionamos novas variáveis de ambiente, é importante **fazer um novo Deploy** na Vercel para que as mudanças tenham efeito. Vá até a aba **Deployments**, clique nos três pontos do último deploy e selecione **Redeploy**.

### 3. Sincronizando o seu Computador (Notebook)
Para autorizar o seu computador a enviar o progresso atualizado para a nuvem:
1. Acesse o site do seu Hub através do seu computador (Notebook), mas adicione o token na URL desta forma:
   `https://hub-calendario-coral.vercel.app/?token=SEU_TOKEN_CRIADO_AQUI`
2. O sistema automaticamente vai ler esse token, salvar no cache do seu navegador e a URL voltará ao normal.
3. A partir desse momento, qualquer item que você marcar ou desmarcar será enviado de forma "silenciosa" (background) para o Vercel KV.

### 4. Sincronizando o seu Celular
No seu celular, você **não** precisa passar o token na URL.
Basta acessar o site normalmente (`https://hub-calendario-coral.vercel.app/`). Sempre que a página carregar, ele vai checar se os dados da nuvem são mais recentes que os locais. Se forem, ele irá atualizar a visualização com o seu progresso do computador.
