# Hub de Estudos V4 — Gabriel Falcao da Cruz

Hub pessoal, hospedado na Vercel, para desenvolvimento tecnico e preparacao para vagas de Backend Java Junior. A V4 preserva o calendario existente e evolui o uso do Hub para medir uma pergunta mais importante: **Gabriel consegue explicar, implementar e defender isso sem ajuda?**

## Foco profissional

- Foco maximo: SQL/PostgreSQL e Testes.
- Foco alto: Backend Java/Spring e Mock Interview.
- Foco medio: DSA essencial e System Design aplicado.
- Continuo: Ingles e Interview Communication.
- Manutencao: Java Core apos a conclusao da trilha.

O SafeWallet e o laboratorio principal. A sequencia recomendada e: conceito → exercicio isolado → SafeWallet → teste → explicacao de entrevista.

## Areas do Hub

1. **Ingles:** preserva as 225 aulas e adiciona Technical English Speaking de 5–10 minutos.
2. **Java Core:** preserva o plano e adiciona Weekly Retrieval sem criar semanas infinitas.
3. **DSA:** prioriza padroes P0/P1 e deixa aprofundamentos como P2/opcionais.
4. **Testes:** JUnit, Mockito, integracao real, PostgreSQL, Testcontainers, rollback e concorrencia.
5. **SQL + PostgreSQL:** fundamentos, queries, indices, EXPLAIN, transacoes, isolamento, locks, deadlocks e idempotencia.
6. **Interview Communication:** projetos, respostas comportamentais e treino de 20s/60s/3min.
7. **System Design:** oito drills semanais para problemas realistas de backend.
8. **Mock Interview:** rotacao curta de segunda a sabado usando ChatGPT por voz, sem integracao de API.

## Filosofia de estudo

Estudar → implementar → explicar → ser questionado → corrigir → repetir → demonstrar em projeto real.

- Data passada nao significa competencia concluida.
- Checkpoints so sao marcados depois de demonstracao real.
- Feynman de checkpoint e feito sem IA.
- Nao empilhar duas trilhas para recuperar atraso; usar os buffers e manter a ordem pedagogica.
- Segunda a sexta, 19h–22h, permanece reservado para Escola da Nuvem — Developer.
- Coverage nao e qualidade; comportamentos criticos recebem prioridade.

## System Design

Cada drill usa o mesmo roteiro: requisitos, perguntas de esclarecimento, fluxo minimo, dados/estado, concorrencia, falhas, escala, trade-offs e tecnologia. O Hub reforca que tecnologia — inclusive AWS — vem por ultimo.

## Mock Interview

Rotacao: Java/Spring, SQL/Backend, Projetos/Curriculo, System Design, Testes e Comportamental. Durante a sessao: responder sem material, receber follow-up, explorar profundidade e somente depois avaliar clareza, correcao, concisao, trade-offs e pontos de revisao.

## Progresso e compatibilidade

- Progresso principal no navegador: `hubGabrielV3`.
- Data real de inicio: `hub_startedAt`.
- Check-ins separados: `hubGabrielStudyLog`.
- Token local de sincronizacao: `syncToken`.
- Chave Redis: `hubGabrielV3_progress`.

IDs antigos nao foram renomeados. Os IDs V4 comecam incompletos e entram no mesmo objeto de progresso. Technical English e Java Weekly Retrieval sao rotinas auxiliares e nao inflam o percentual global.

## Sincronizacao

`api/progress.js` usa `@upstash/redis`:

- `GET /api/progress` le o JSON salvo.
- `POST /api/progress` exige o header `x-hub-token`.
- Variaveis da Vercel: `KV_REST_API_URL`, `KV_REST_API_TOKEN` e `PROGRESS_SYNC_TOKEN`.

Nenhum segredo deve ser commitado. Para autorizar um navegador, abra uma vez `/?token=SEU_TOKEN`; o frontend salva o valor apenas no `localStorage` e remove o parametro da URL.

## Execucao e validacao

O frontend e estatico: abra `index.html` ou sirva a pasta com um servidor local. A sincronizacao remota depende do ambiente Vercel.

```bash
npm test
npm run test:sql
```

Os testes verificam sintaxe JavaScript, IDs unicos, 225 aulas de Ingles, trilhas V4, datas, progresso global, compatibilidade com registros legados e persistencia apos recarregar.
