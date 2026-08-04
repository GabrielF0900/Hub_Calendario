# Prompt para Claude Code — Atualizar Hub de Estudos (index.html)

> Copie tudo a partir da linha abaixo e cole no Claude Code, rodando na pasta onde está o `index.html` do Hub.

---

Você vai atualizar o arquivo `index.html` do meu Hub de Estudos (Java Core, DSA, Testes, SQL, Storytelling, Inglês). Antes de mudar qualquer coisa, leia o arquivo inteiro e entenda os padrões já existentes:

- Objeto `NEW_TRACKS` (javacore, dsa, testes, sql, storytelling) com `weeks[].topics[].subtopics[]`.
- `THEME` com cores por trilha, aplicadas via `--tc`/`--tg` CSS vars.
- Persistência em `localStorage` (chave `SKEY = 'hubGabrielV3'`), funções `store()`, `isDone(id)`, `setDone(id,v)`, e `syncCloud(data)` que envia pra `/api/progress` se houver `syncToken`.
- Modal genérico (`#detailModal`, funções `openTrackModal`, `showModal`, `closeModal`) que mostra `m-why`, `m-subtopics-list`, `m-feynman`.
- Cada subtópico tem um `id` único (ex: `jc_1_1_1`) usado como chave no localStorage.

**Não quebre a estrutura de dados existente nem os ids de subtópicos já criados** — todo progresso salvo no localStorage do usuário depende desses ids continuarem os mesmos.

Faça as 4 mudanças abaixo, nesta ordem:

---

## 1. Adicionar 3 tópicos que faltam na trilha Java Core

Comparei o roadmap.sh/java oficial com a trilha `javacore` já implementada. Dois tópicos do gap (Exception Handling e Optional) já estão cobertos em `jc_1_3` e `jc_1_4` — não mexer nesses. Faltam 3, que devem ser adicionados como um novo tópico na Semana 4 (que hoje só tem `jc_1_7`, então há espaço) ou, se preferir, um novo tópico curto na Semana 5 antes da revisão. Use seu julgamento sobre onde encaixar melhor sem sobrecarregar um único dia, mas mantenha o padrão de 1 tópico por dia de estudo (Segunda/Quarta).

Novo tópico a criar (siga exatamente o schema de `topics[]` — `id`, `title`, `schedule`, `estimatedTime`, `description`, `subtopics[]` com `id`+`text`):

- **Título sugerido:** "1.8 Enums, Overload e Pass by Value"
- **Subtópicos:**
  1. Enums — para que servem além de constantes, exemplo com método dentro de um enum
  2. Method Overloading vs Overriding — diferença prática (mesmo nome, assinatura diferente vs mesmo nome/assinatura em subclasse) — pergunta clássica de entrevista
  3. Pass by Value vs Pass by Reference — por que Java é sempre pass-by-value (mesmo para objetos, a referência é copiada por valor) — pegadinha clássica

Escreva a `description` no mesmo tom didático dos outros tópicos (explique por que isso é cobrado em entrevista, não só o que é).

---

## 2. Modal "Como Vamos Estudar" (metodologia)

Crie um novo modal (ou reaproveite o padrão visual do `#detailModal`) acessível por um botão/ícone no header ou perto do card "Como Começar", com o conteúdo abaixo. Pode ser um modal separado (`#methodModal`) para não conflitar com o modal de tópicos.

**Conteúdo do modal, em seções:**

**a) Hierarquia de fontes (primária → secundária → terciária)**
- Primária: Rocketseat (aula estruturada, ponto de partida padrão)
- Secundária: roadmap.sh/java — não é fonte de conteúdo nova, é mapa de verificação de cobertura. Quando a Rocketseat não tiver o assunto, abrir o nó correspondente no roadmap.sh e seguir o link recomendado de lá.
- Terciária: Baeldung.com — fonte de prática/aprofundamento em qualquer um dos casos acima, e fonte primária de fallback quando nem Rocketseat nem roadmap.sh cobrirem bem.
- DSA usa NeetCode (primária) + LeetCode/HackerRank (prática). SQL usa SQLZoo (primária) + HackerRank SQL (prática).

**b) Prática Feynman**
- Reaproveitar o texto que já existe em `tr.feynmanPractice` de cada trilha como referência, mas aqui explicar o método em geral: gravar em voz alta explicando o tópico como se fosse pra um entrevistador, sem jargão não explicado, ouvir de volta e marcar onde travou.

**c) Regra de recuperação de atraso (ordem > rótulo do dia)**
- O que importa é a ordem do conteúdo, não o dia da semana marcado no calendário. Se perder um dia, fazer o próximo conteúdo na ordem certa, não pular pra "ficar em dia com a data".
- Nunca empilhar dois blocos de trilhas diferentes no mesmo dia pra compensar atraso.
- O buffer de sábado (já existente no painel `saturdayBlockPanel`) absorve o que sobrar da semana.

**d) NotebookLM**
- Não é fonte de conteúdo nova — é onde consolidar o que já foi consumido (anotações, artigos, resumos) pra revisar depois e testar o próprio entendimento.

---

## 3. Sistema de check-in de dias estudados (log real, separado do progresso por tópico)

Hoje o app só marca "subtópico concluído" (`isDone(id)` por subtópico). Preciso de algo adicional: um **registro dos dias reais em que efetivamente estudei**, independente de quantos subtópicos completei naquele dia. Objetivo: no fim, eu conseguir ver um histórico tipo "estudei nos dias X, Y, Z" pra reorganizar minha rotina depois.

**Requisitos:**
- Nova estrutura no localStorage (pode ser uma nova chave, ex: `hubGabrielStudyLog`, ou um campo dentro do objeto existente — decida o que for mais simples de manter sincronizado com `syncCloud`).
- Cada entrada do log: `{ date: 'YYYY-MM-DD', trackId: 'javacore', note: '' }` (note opcional).
- Interface simples: um botão "✅ Marquei que estudei hoje" na aba de cada trilha, que registra a data atual + trilha ativa. Também precisa de uma forma de ver/editar o histórico (uma lista ou um mini-calendário mostrando os dias marcados), com opção de remover uma marcação feita errada.
- Isso é **separado** do sistema de subtópicos concluídos — dá pra ter estudado um dia e não ter marcado nenhum subtópico como concluído ainda (ex: assisti a aula mas não terminei os exercícios), e vice-versa.

---

## 4. Botão "INICIAR" — sistema automático de organização de rotina

Hoje as datas de cada trilha (`startDate`, `endDate` em `NEW_TRACKS`) são strings fixas (ex: `"03/08/2026"`). O plano original previa começar em 03/08/2026, mas isso não aconteceu ainda porque ainda estamos organizando o Hub. Preciso que isso vire dinâmico:

**Requisitos:**
- Adicionar um botão **"▶ INICIAR"** visível quando uma trilha ainda não foi iniciada (ex: perto do header da trilha, ou um estado global "hub ainda não iniciado").
- Ao clicar em INICIAR (pela primeira vez, para o Hub como um todo ou por trilha — decida a abordagem mais simples: um único "Iniciar Hub" que dispara todas as trilhas a partir de hoje, respeitando a ordem/offset relativo que já existe entre elas, é preferível a botões separados por trilha, pra não perder a lógica de "Java Core antes de DSA").
- O sistema deve:
  1. Capturar a data real de hoje como novo "dia 1".
  2. Recalcular `startDate`/`endDate` de cada trilha mantendo os offsets relativos que já existem hoje entre elas (ex: hoje DSA começa 1 dia depois de Java Core, Testes começa numa sexta especifica — preserve essas distâncias relativas, só deslocando o ponto de partida pra data real de início).
  3. Recalcular os `dateRange` de cada semana dentro de cada trilha (`weeks[].dateRange`) e o `schedule` de cada tópico, de forma equivalente ao que já é feito pra Inglês com a função `addDays(START, ...)` — ou seja, gerar as datas programaticamente a partir de uma constante de início, em vez de strings fixas.
  4. Salvar esse "dia de início real" no localStorage, pra persistir entre sessões (ex: `hub_startedAt`).
  5. Recalcular o progresso (`updateProgress`) considerando essa nova data.
- **Manter a opção manual**: independente do botão INICIAR, deve continuar sendo possível marcar manualmente o início e o fim de um bloco de estudo (o check-in do item 3 já cobre isso a nível de dia — pode reaproveitar a mesma estrutura, sem duplicar lógica).
- Antes de clicar em INICIAR, o Hub deve continuar 100% navegável (visualizar trilhas, tópicos, modais) — só o cálculo de progresso por data/prazo fica pendente até o clique.

---

## Restrições gerais

- Mantenha o design system atual (cores do `THEME`, fontes, classes Tailwind já usadas) — não redesenhe do zero.
- Não quebre a sincronização em nuvem existente (`syncCloud`/`/api/progress`).
- Teste que o localStorage antigo (progresso já salvo) continua funcionando após as mudanças — não renomeie ids de subtópicos já existentes.
- Ao final, me dê um resumo do que foi alterado e quais chaves novas de localStorage foram criadas, pra eu saber o que existe no armazenamento.
