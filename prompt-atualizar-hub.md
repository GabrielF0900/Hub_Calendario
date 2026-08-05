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

Faça as mudanças abaixo, nesta ordem:

---

## 1. Adicionar 3 tópicos que faltam na trilha Java Core

Comparei o roadmap.sh/java oficial com a trilha `javacore` já implementada. Dois tópicos do gap (Exception Handling e Optional) já estão cobertos em `jc_1_3` e `jc_1_4` — não mexer nesses. Faltam 3, que devem ser adicionados como um novo tópico na Semana 4. Use seu julgamento sobre onde encaixar melhor sem sobrecarregar um único dia, mas mantenha o padrão de 1 tópico por dia de estudo (Segunda/Quarta).

Novo tópico a criar (siga exatamente o schema de `topics[]` — `id`, `title`, `schedule`, `estimatedTime`, `description`, `subtopics[]` com `id`+`text`):

- **Título sugerido:** "1.8 Enums, Overload e Pass by Value"
- **Subtópicos:**
  1. Enums — para que servem além de constantes, exemplo com método dentro de um enum
  2. Method Overloading vs Overriding — diferença prática (mesmo nome, assinatura diferente vs mesmo nome/assinatura em subclasse) — pergunta clássica de entrevista
  3. Pass by Value vs Pass by Reference — por que Java é sempre pass-by-value (mesmo para objetos, a referência é copiada por valor) — pegadinha clássica

Escreva a `description` no mesmo tom didático dos outros tópicos (explique por que isso é cobrado em entrevista, não só o que é).

**⚠️ Atenção ao campo `schedule` desse tópico:** se o encaixe for na Semana 4, o slot disponível é **Quarta, 26/08 às 13h** (não 27/08 — 27/08/2026 é quinta-feira; 26/08/2026 é a quarta correta, confirmado com `datetime`).

---

## 2. Modal "Como Vamos Estudar" — já existe, não recriar

O modal `#methodModal` com o botão "📚 Como Estudar" **já está implementado** no arquivo. **Não toque nele.** Pule esta etapa completamente.

---

## 3. Sistema de check-in de dias estudados (log real, separado do progresso por tópico)

**Requisitos:**
- Nova estrutura no localStorage (pode ser uma nova chave, ex: `hubGabrielStudyLog`, ou um campo dentro do objeto existente — decida o que for mais simples de manter sincronizado com `syncCloud`).
- Cada entrada do log: `{ date: 'YYYY-MM-DD', trackId: 'javacore', note: '' }` (note opcional).
- Interface simples: um botão "✅ Marquei que estudei hoje" na aba de cada trilha, que registra a data atual + trilha ativa. Também precisa de uma forma de ver/editar o histórico (uma lista ou um mini-calendário mostrando os dias marcados), com opção de remover uma marcação feita errada.
- Isso é **separado** do sistema de subtópicos concluídos — dá pra ter estudado um dia e não ter marcado nenhum subtópico como concluído ainda.

---

## 4. Botão "INICIAR" — sistema automático de organização de rotina

**Requisitos:**
- Adicionar um botão **"▶ INICIAR"** visível quando uma trilha ainda não foi iniciada.
- Ao clicar em INICIAR (pela primeira vez, para o Hub como um todo ou por trilha — prefira um único "Iniciar Hub" que dispara todas as trilhas a partir de hoje, respeitando a ordem/offset relativo que já existe entre elas).
- O sistema deve:
  1. Capturar a data real de hoje como novo "dia 1".
  2. Recalcular `startDate`/`endDate` de cada trilha mantendo os offsets relativos que já existem hoje entre elas.
  3. Recalcular os `dateRange` de cada semana (`weeks[].dateRange`) e o `schedule` de cada tópico programaticamente a partir de uma constante de início.

     **⚠️ Atenção especial ao recalcular `schedule`** — o arquivo tem **três formatos distintos** que devem ser preservados corretamente:
     - **Formato Java Core (data única com hora):** `"Quarta, 26/08 às 13h"` → ao recalcular, manter `"DiaDaSemana, DD/MM às HHh"`.
     - **Formato DSA (duas datas com hora no final):** `"Ter 04/08 + Qui 06/08 às 13h"` → ao recalcular, detectar as **duas datas** com regex `/\d{2}\/\d{2}/g` (flag `g`), recalcular ambas, e remontar no formato `"Dia DD/MM + Dia DD/MM às HHh"`.
     - **Formato revisão (sem data, só dia da semana):** `"Seg e Qua às 13h"` → **não alterar**.

     Antes de implementar, verificar se SQL e Storytelling têm formatos de `schedule` adicionais — adapte o parser se necessário.

  4. Salvar esse "dia de início real" no localStorage (ex: `hub_startedAt`).
  5. Recalcular o progresso (`updateProgress`) considerando essa nova data.

**Consistência de estilo:**
Use sempre o nome **completo** do dia da semana (ex: `"Segunda"`, `"Terça"`, `"Quarta"`, `"Quinta"`, `"Sexta"`, `"Sábado"`) em todos os caminhos do código de recalculação.

---

## Restrições gerais

- Mantenha o design system atual.
- Não quebre a sincronização em nuvem existente.
- Teste que o localStorage antigo (progresso já salvo) continua funcionando após as mudanças — não renomeie ids de subtópicos já existentes.
- Ao final, me dê um resumo do que foi alterado e quais chaves novas de localStorage foram criadas, pra eu saber o que existe no armazenamento.
