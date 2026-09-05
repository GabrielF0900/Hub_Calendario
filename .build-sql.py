import json
from pathlib import Path

p = Path('index.html')
html = p.read_text(encoding='utf-8')
modules = [
 'Introdução ao Mundo dos Bancos de Dados', 'Manipulação Básica de Dados',
 'Modelagem de Dados Essencial', 'Mini Projeto: Modelando um sistema simples',
 'Consultas Avançadas', 'Relacionamentos e Junções',
 'Consultas Avançadas e Subconsultas', 'Otimização e Performance',
 'Recursos Avançados do Postgres', 'Projeto Final', 'Tópicos Especiais para o Mercado'
]
sessions=[]
def s(module, title, minutes, study, practice, review='', note='', kind='estudar'):
    sessions.append(dict(module=module,title=title,minutes=minutes,study=study,practice=practice,review=review,note=note,kind=kind))

# Sessões pedagógicas; títulos de sessão/conceitos não são títulos de vídeos.
# Semana 1
s(0,'Introdução a bancos de dados',60,['Introdução ao professor; introdução ao mundo dos bancos de dados','Importância, tipos de bancos de dados e bancos relacionais'],['Identificar dados e relações em um sistema do cotidiano'])
s(0,'SQL e preparação do PostgreSQL',75,['Introdução ao SQL e ao PostgreSQL','Instalação e configuração do PostgreSQL'],['Conferir a instalação e a conexão local'])
s(0,'Beekeeper Studio e primeiro banco',60,['Instalação e configuração do Beekeeper Studio','Criação do primeiro banco de dados'],['Conectar o Beekeeper ao PostgreSQL e criar um banco de estudo'])
s(0,'Entendendo tabelas',45,['Conceito de tabela; reconhecer linhas, colunas e relações'],['Explorar o primeiro banco e desenhar uma tabela simples no papel'],'Explicar a relação entre banco, tabela e registro')
s(0,'Consolidação da introdução',45,[],['Atividade/quiz do módulo Introdução ao Mundo dos Bancos de Dados'],'Revisar somente os erros e conferir PostgreSQL + Beekeeper funcionando',kind='revisar')
# Semana 2
s(1,'CREATE e tipos numéricos',75,['Operações básicas; estrutura e execução do CREATE','Tipos de dados numéricos no PostgreSQL'],['Escrever manualmente um CREATE TABLE e conferir a estrutura no Beekeeper'])
s(1,'Escolhendo os tipos de dados',75,['Tipos textuais e booleanos','UUID, tipos seriais, ARRAY e JSON'],['Criar uma pequena tabela de teste com os tipos apresentados'])
s(1,'INSERT e SELECT',75,['Estrutura e execução do INSERT','Visualização da estrutura da tabela no Beekeeper; estrutura e execução do SELECT'],['Inserir poucos registros e escrever 2 consultas SELECT manualmente'],'Feynman curto: explicar INSERT e SELECT linha por linha')
s(1,'UPDATE e DELETE',75,['Estrutura e execução do UPDATE','Estrutura e execução do DELETE'],['Reproduzir os comandos em dados de estudo e conferir o resultado com SELECT'],'Feynman curto: explicar as alterações e o alcance de cada comando')
s(1,'Revisão de CRUD',60,[],['Atividade/quiz do módulo Manipulação Básica de Dados','Escrever um pequeno fluxo CREATE, INSERT, SELECT, UPDATE e DELETE'],'Revisar erros de CRUD e explicar uma query sem consultar',kind='revisar')
# Semana 3
s(2,'Modelo Entidade-Relacionamento',75,['Introdução à modelagem de dados e ao Modelo Entidade-Relacionamento','Entidades, atributos, relacionamentos e cardinalidade'],['Rascunhar um modelo ER com 3 entidades'])
s(2,'Chaves e integridade',90,['Chaves primárias (PK) e chaves estrangeiras (FK)'],['Definir PK/FK e cardinalidades no modelo de estudo'],'Feynman curto: explicar como PK/FK protegem os relacionamentos')
s(2,'Introdução à normalização',75,['Funcionamento da normalização; regras de transformação','Conceitos de formas normais e redundância'],['Identificar redundâncias em uma tabela de exemplo'],'Explicar o problema que a normalização resolve')
s(2,'Primeira e segunda formas normais',90,['1FN e 2FN'],['Transformar um exemplo em 1FN e depois em 2FN'],'Feynman curto: justificar cada separação de tabela')
s(2,'Terceira forma normal e DER',90,['3FN; formas normais adicionais quando apresentadas pela Rocketseat','Diagramas ER / DER e exemplos práticos'],['Aplicar 3FN e atualizar o DER'],'Feynman curto: explicar a normalização do modelo')
# Semana 4
s(2,'Do ER para tabelas e constraints',90,['Mapeamento ER para modelo relacional','Tabelas e constraints; criação de tabelas e constraints'],['Implementar o modelo relacional com PK/FK e constraints no PostgreSQL'])
s(2,'CRUD aplicado e revisão de fundamentos',90,[],['Aplicar INSERT, SELECT, UPDATE e DELETE ao modelo','Atividade/quiz de Modelagem de Dados Essencial e Quiz - Fundamentos'],'Revisar erros de CRUD, PK/FK e normalização; explicar uma query',kind='revisar')
s(3,'Mini projeto: gestão educacional',75,[],['Acompanhar a proposta do sistema de gestão educacional na Rocketseat','Identificar entidades, atributos e relacionamentos'],note='Projeto oficial do nível Fundamentos.',kind='pratica')
s(3,'Mini projeto: normalização e DER',90,[],['Normalizar os dados do sistema educacional','Elaborar DER e mapear para o modelo relacional'],'Explicar as cardinalidades e as escolhas de PK/FK',kind='pratica')
s(3,'Mini projeto: implementação',90,[],['Implementar as tabelas do sistema educacional no PostgreSQL','Validar constraints e inserir poucos dados para conferir o modelo'],'Revisar o mini projeto com o material Rocketseat',kind='pratica')
# Semana 5
s(4,'WHERE e operadores',60,['Subtipos/tipos relevantes do SQL apresentados no curso','WHERE, operadores de comparação, AND e OR'],['Escrever 3 filtros manuais em dados de estudo'])
s(4,'Filtros e resultados ordenados',75,['IN, NOT IN, BETWEEN e LIKE','DISTINCT, ORDER BY e LIMIT'],['Prática complementar: 3 a 5 exercícios de WHERE no SQLZoo após as aulas'],'Revisar os erros dos filtros')
s(4,'Funções de agregação',60,['COUNT, SUM, AVG, MAX e MIN'],['Escrever 3 consultas de agregação e conferir os resultados'])
s(4,'GROUP BY e HAVING',90,['GROUP BY, HAVING e agregações'],['Criar um relatório agrupado e filtrar os grupos'],'Feynman curto: explicar GROUP BY, HAVING e a diferença para WHERE',note='Opcional: relatório de total de transações por usuário no SafeWallet.')
s(4,'Funções e relatórios',75,['Manipulação de strings e números','Manipulação de datas quando abordada; consultas de relatório'],['Reproduzir as funções ensinadas e escrever um relatório curto'])
# Semana 6
s(4,'Relacionamentos nas consultas',75,['Revisão de relacionamentos e JOINs abordados no módulo'],['Reproduzir uma junção do curso e verificar as correspondências'],'Explicar a ligação entre PK/FK e a consulta')
s(4,'Consolidação de consultas',60,[],['Atividade/quiz do módulo Consultas Avançadas','Prática complementar: 2 a 3 exercícios de agregação no HackerRank SQL Basic/Intermediate'],'Revisar WHERE, GROUP BY e HAVING com base nos erros',kind='revisar')
s(5,'INNER JOIN e LEFT JOIN',90,['INNER JOIN e LEFT JOIN'],['Escrever duas consultas e comparar linhas com e sem correspondência'],'Feynman curto: explicar JOIN linha por linha',note='Opcional: consultar usuários + transações no banco do SafeWallet.')
s(5,'Consultas com múltiplas tabelas',90,['Relacionamentos entre tabelas e consultas com múltiplas tabelas','RIGHT JOIN e FULL JOIN, caso constem no conteúdo Rocketseat'],['Consultar 3 tabelas e conferir cardinalidade e duplicações'],'Revisar somente as junções que causaram dúvida')
s(5,'Subqueries',90,['Subqueries; subconsultas correlacionadas quando abordadas'],['Escrever 2 subconsultas a partir dos exemplos do curso'],'Feynman curto: explicar a consulta interna e a externa')
# Semana 7
s(5,'Common Table Expressions',90,['Common Table Expressions (CTE) e WITH'],['Reescrever uma consulta em etapas com WITH'],'Feynman curto: explicar cada CTE e o resultado final')
s(5,'Operações de conjunto',75,['UNION, INTERSECT e operações de conjunto'],['Comparar os resultados de duas operações sobre dados pequenos'])
s(5,'Window Functions',90,['Window Functions / funções de janela'],['Reproduzir uma função de janela e comparar com GROUP BY'],'Feynman curto: explicar o que a janela calcula sem perder as linhas')
s(5,'Consultas analíticas',75,['Consultas analíticas combinando os conceitos do módulo'],['Escrever uma consulta analítica e conferir o resultado manualmente'])
s(5,'Revisão de consultas e modelagem',75,[],['Atividade/quiz de Relacionamentos e Junções e Quiz - Consultas e Modelagem','Prática complementar: 2 exercícios de JOIN no SQLZoo ou HackerRank'],'Revisar erros de JOIN, subquery, CTE e funções de janela',kind='revisar')
# Semana 8: classificação exibida na descrição pública oficial.
s(6,'Consultas complexas e estratégias',75,['Consultas complexas, subconsultas e estratégias de consulta'],['Comparar duas formas de escrever uma consulta com o mesmo resultado'])
s(6,'Índices na prática',90,['Índices: criação e utilização'],['Criar um índice em uma tabela de estudo e testar a consulta'],'Feynman curto: explicar o benefício e o custo do índice')
s(6,'Planos de execução',90,['Análise de performance e planos de execução','EXPLAIN e EXPLAIN ANALYZE'],['Comparar os planos de uma consulta antes e depois de um índice'],'Explicar as diferenças observadas no plano',note='Opcional: usar EXPLAIN ANALYZE em uma consulta de leitura do SafeWallet.')
s(6,'Particionamento e volume de dados',75,['Particionamento; boas práticas de performance'],['Reproduzir o exemplo de particionamento apresentado e registrar quando faz sentido'])
s(6,'Normalização vs denormalização',75,['Normalização vs denormalização e otimização de consultas'],['Atividade/quiz do módulo Consultas Avançadas e Subconsultas'],'Justificar o trade-off em um exemplo do curso')
# Semana 9: não atribuir títulos de aulas indisponíveis à Rocketseat.
s(7,'Otimização e Performance: conteúdo do módulo',75,['Acompanhar o início do módulo Otimização e Performance na ordem da plataforma'],['Executar os exemplos apresentados nesta primeira parte'],note='A descrição pública deste módulo repete a de Recursos Avançados do Postgres. Os títulos individuais não estão disponíveis; siga as aulas reais, inclusive se introduzirem views, funções ou transações.')
s(7,'Otimização e Performance: continuação',75,['Continuar as aulas do módulo Otimização e Performance na ordem da plataforma'],['Executar os exemplos restantes e registrar dúvidas'],note='Retome do ponto anterior; os blocos são estimativas de estudo com prática, não títulos oficiais de vídeos.')
s(7,'Análise e execução eficiente',90,[],['Prática de consolidação: analisar uma consulta já estudada com EXPLAIN ANALYZE','Testar uma melhoria de consulta ou índice e comparar resultado e plano'],'Revisar erros e justificar a estratégia de otimização',kind='pratica')
s(7,'Estratégias para grandes volumes',75,[],['Consolidar performance de banco: relacionar índices, particionamento e volume de dados','Registrar uma estratégia de execução eficiente baseada nos exemplos estudados'],'Explicar os limites da estratégia escolhida',kind='revisar')
s(7,'Consolidação de performance',60,[],['Atividade/quiz do módulo Otimização e Performance'],'Revisar somente dúvidas sobre análise de consultas e os recursos efetivamente apresentados',kind='revisar')
# Semana 10
s(8,'Views e tabelas temporárias',90,['Views, criação de Views e tabelas temporárias'],['Criar uma View e reproduzir o uso de uma tabela temporária'],'Feynman curto: explicar a consulta da View')
s(8,'Funções PostgreSQL',75,['Funções PostgreSQL'],['Criar e executar uma função simples seguindo o curso'])
s(8,'PL/pgSQL',90,['PL/pgSQL e funções no contexto apresentado'],['Implementar um exemplo curto de função em PL/pgSQL'],'Explicar entradas, processamento e retorno')
s(8,'Triggers',90,['Triggers e automação no PostgreSQL'],['Criar uma trigger e validar o evento que a aciona'],'Feynman curto: explicar quando e por que a trigger executa')
s(8,'Stored procedures',90,['Stored procedures e sua utilização'],['Reproduzir uma procedure do curso e conferir os efeitos'],'Distinguir as responsabilidades de função, trigger e procedure')
# Semana 11
s(8,'Transações',90,['Transactions: BEGIN, COMMIT e ROLLBACK','Propriedades e conceitos transacionais abordados no curso'],['Executar um fluxo com COMMIT e outro com ROLLBACK em dados de estudo'],'Feynman curto: explicar a unidade de trabalho da transação',note='Opcional: relacionar o conceito com @Transactional no Spring; a aplicação Java fica para depois.')
s(8,'Segurança e permissões',90,['Segurança, usuários, roles e permissões','GRANT e REVOKE'],['Criar uma role de estudo e testar concessão e revogação de acesso'])
s(8,'Backup e restauração',90,['Backup, restauração e administração básica de PostgreSQL'],['Gerar um backup do banco de estudo e restaurar em outro banco','Conferir tabelas e dados restaurados'])
s(8,'Revisão avançada aplicada',75,[],['Revisar uma consulta com subquery/CTE e seu índice','Validar uma transação e uma View em um cenário pequeno'],'Feynman curto: explicar índice, transação, View e trigger; revisar só os pontos de dúvida',kind='revisar')
s(8,'Fechamento de técnicas avançadas',60,[],['Exercícios e atividade/quiz de Recursos Avançados do Postgres','Quiz - Técnicas Avançadas'],'Revisar os erros antes de iniciar o projeto final',kind='revisar')
# Semana 12
s(9,'Biblioteca Universitária: levantamento',75,[],['Acompanhar a proposta oficial do Sistema de Biblioteca Universitária','Levantar requisitos e identificar entidades, atributos e regras'],kind='pratica')
s(9,'Biblioteca: modelo conceitual e DER',90,[],['Construir o modelo conceitual','Elaborar o DER com relacionamentos e cardinalidades'],'Justificar a modelagem com base nos requisitos',kind='pratica')
s(9,'Biblioteca: modelo relacional',90,[],['Mapear o DER para o modelo relacional','Definir tabelas, constraints, PK e FK'],kind='pratica')
s(9,'Biblioteca: criação do banco',90,[],['Criar o banco e as tabelas no PostgreSQL','Implementar constraints e PK/FK; conferir a estrutura'],kind='pratica')
s(9,'Biblioteca: população e CRUD',90,[],['Popular dados de exemplo seguindo a formação','Implementar e validar INSERT, SELECT, UPDATE e DELETE'],'Explicar um fluxo CRUD do projeto',kind='pratica')
# Semana 13
s(9,'Biblioteca: consultas e joins',90,[],['Implementar consultas e relatórios com relacionamentos/joins','Adicionar consultas avançadas com os recursos adequados já estudados'],'Conferir resultados e explicar uma consulta avançada',kind='pratica')
s(9,'Biblioteca: otimização e índices',90,[],['Analisar planos de execução das consultas do projeto','Criar índices pertinentes e comparar a performance'],kind='pratica')
s(9,'Biblioteca: views e triggers',90,[],['Criar views previstas no projeto','Implementar triggers e validar seu comportamento'],kind='pratica')
s(9,'Biblioteca: procedures e segurança',90,[],['Implementar stored procedures quando aplicável ao projeto','Configurar roles/permissões e testar os acessos previstos'],kind='pratica')
s(9,'Biblioteca: validação final',90,[],['Validar modelagem, integridade, CRUD, consultas e recursos avançados','Concluir a atividade do Projeto Final e registrar a revisão final'],'Explicar o projeto e revisar somente falhas encontradas',kind='pratica')
# Semana 14
s(10,'Big Data e integração com API',75,['Big Data relacionado a bancos relacionais','Integração banco + API usando Node.js — conceito transferível'],['Acompanhar a demonstração e identificar o caminho da requisição até o banco'],note='Na trilha, a Rocketseat demonstra com Node.js. Foque no conceito; posteriormente ele será aplicado em Java/Spring.')
s(10,'CRUD por API — conceito transferível',75,['Conceitos de CRUD por API; Node.js apenas no contexto da formação'],['Reproduzir o exemplo do curso e relacionar as operações da API ao SQL'],note='Na trilha, a Rocketseat demonstra com Node.js. Foque no conceito; posteriormente ele será aplicado em Java/Spring.')
s(10,'NoSQL e MongoDB',60,['Bancos NoSQL e MongoDB'],['Comparar o modelo de documentos apresentado com um modelo relacional'])
s(10,'JSON, tipos complexos e produção',75,['JSON e tipos complexos no PostgreSQL','Monitoramento de bancos em produção e manutenção de banco'],['Executar um exemplo de JSON e registrar os cuidados de monitoramento apresentados'])
s(10,'Tendências e conclusão da jornada',60,['Tendências e evolução dos bancos de dados'],['Atividade/quiz de Tópicos Especiais para o Mercado e Quiz - Projeto e Aplicações Práticas'],'Revisar os erros e registrar próximos passos de aplicação em Backend Java',kind='revisar')

assert len(sessions)==70
track=dict(id='sql',title='SQL + PostgreSQL',emoji='🗄️',order=5,totalWeeks=14,
    startDate='Ao iniciar o Hub',endDate='Sexta da semana 14',color='#06b6d4',
    frequency='Segunda a sexta · manhã · 45–90 min',
    source='Rocketseat — Banco de Dados',
    courseTitle='Banco de dados, na prática: do básico ao avançado com PostgreSQL',
    sourceUrl='https://app.rocketseat.com.br/journey/banco-de-dados/contents',
    whyStudy='Jornada Rocketseat Banco de Dados, do básico ao avançado com PostgreSQL, com foco em Backend Java. Assista às aulas correspondentes aos conceitos da sessão, execute os comandos, escreva algumas queries manualmente e revise os erros. Os tempos incluem estudo e prática; não são durações oficiais de vídeos. Se o bloco terminar, retome do ponto em que parou, sem acumular sessões.',
    feynmanPractice='Depois de escrever uma query, explique em voz alta linha por linha o que ela faz. Se não souber explicar uma cláusula, revise apenas aquela parte.',
    weeks=[])
for wi in range(14):
    week=dict(weekNum=wi+1,startOffset=wi*7,dateRange=f'Semana {wi+1} · segunda a sexta · manhã',isReviewWeek=False,topics=[])
    for di, x in enumerate(sessions[wi*5:wi*5+5]):
        n=wi*5+di+1
        level=1 if x['module']<4 else 2 if x['module']<6 else 3 if x['module']<9 else 4
        desc=f"Nível {level} · {modules[x['module']]}. "
        desc+= 'Sessão de consolidação: pratique e revise apenas os pontos de dúvida.' if x['kind']!='estudar' else 'Assista às aulas correspondentes na Rocketseat e execute os exemplos. Inclua a prática abaixo dentro do tempo da sessão.'
        if x['note']: desc+=' '+x['note']
        subs=[]
        for activity, texts in [('estudar',x['study']),('pratica',x['practice']),('revisar',[x['review']] if x['review'] else [])]:
            for text in texts:
                subs.append(dict(id=f'sql_rs_{n:02}_{len(subs)+1:02}',activityType=activity,text=text))
        week['topics'].append(dict(id=f'sql_rs_session_{n:02}',title=x['title'],dayOffset=wi*7+di,
            schedule=['Segunda','Terça','Quarta','Quinta','Sexta'][di]+' · manhã',
            estimatedTime=f"{x['minutes']} minutos",activityType=x['kind'],block=modules[x['module']],
            description=desc,subtopics=subs))
    track['weeks'].append(week)
start=html.index('  "sql": {')
end=html.index('  "storytelling": {',start)
html=html[:start]+'  "sql": '+json.dumps(track,ensure_ascii=False,indent=2).replace('\n','\n  ')+',\n'+html[end:]

def replace(old,new):
    global html
    assert old in html,old[:100]
    html=html.replace(old,new)

replace('S&aacute;b 08/08/2026</div>','<span id="sqlEntryDate">Segunda da semana 1</span></div>')
replace('S&aacute;b &middot; 13h-13h50','Seg–Sex &middot; manhã &middot; 45–90 min')
replace('Bloco do S&aacute;bado — 13h &agrave;s 15h (2 horas no total)','Bloco do S&aacute;bado — Storytelling e buffer opcional')
replace('&#9200; 13h00 &ndash; 13h50 &middot; 50min','&#9200; Manhã &middot; opcional')
replace('class="text-sm font-bold text-slate-100 mb-1.5">&#x1F5C4;&#xFE0F; SQL</div>','class="text-sm font-bold text-slate-100 mb-1.5">&#x1F5C4;&#xFE0F; SQL — Buffer / Revisão</div>')
replace('Conte&uacute;do da trilha SQL da semana. Come&ccedil;a em 08/08/2026 e ocorre todo s&aacute;bado.','Use apenas se houver conteúdo SQL pendente na semana. Se estiver em dia, utilize para revisão leve ou descanso. O estudo regular de SQL acontece de segunda a sexta pela manhã.')
replace('<span class="text-cyan-400 font-bold">SQL:</span> SQLZoo (prim&aacute;ria) + HackerRank SQL (pr&aacute;tica)', '<span class="text-cyan-400 font-bold">SQL:</span> 1ª Rocketseat — jornada Banco de Dados (ensino); 2ª SQLZoo (prática complementar); 3ª HackerRank SQL (exercícios); 4ª PostgreSQL Documentation (consulta técnica opcional). Pratique nas plataformas somente depois de estudar o assunto na Rocketseat.')
replace('<!-- c) Regra de recupera&ccedil;&atilde;o -->','<p class="text-[11px] text-cyan-300 leading-relaxed">SQL — Feynman: Depois de escrever uma query, explique em voz alta linha por linha o que ela faz. Se não souber explicar uma cláusula, revise apenas aquela parte.</p>\n\n      <!-- c) Regra de recupera&ccedil;&atilde;o -->')
replace("sql:          { startOff: 5,  totalDays: 77 },  // 08/08 → 24/10 = 77 dias", "sql:          { startOff: 0,  totalDays: NEW_TRACKS.sql.weeks.at(-1).topics.at(-1).dayOffset }, // Segunda da S1 até sexta da última semana")
replace("sub.textContent=`${tr.emoji} Ordem #${tr.order} \\u00b7 ${tr.totalWeeks} semanas \\u00b7 ${tr.frequency}`;", "sub.textContent=tid==='sql'\n      ? `${tr.emoji} ${tr.title} · ${tr.totalWeeks} semanas · ${trackTotal(tid)} subtópicos · manhã · Rocketseat`\n      : `${tr.emoji} Ordem #${tr.order} \\u00b7 ${tr.totalWeeks} semanas \\u00b7 ${tr.frequency}`;")
replace('  updateProgress();\n  const mc=', "  updateProgress();\n  const sqlEntry=document.getElementById('sqlEntryDate');\n  if(sqlEntry) sqlEntry.textContent=getHubStartDate() ? 'Seg '+getEffectiveTrackDates('sql').startDate : 'Segunda da semana 1';\n  const mc=")
replace("  container.innerHTML=`\n  <div class=\"lg:col-span-3 flex flex-col gap-4\">", "  container.innerHTML=`\n  <div class=\"lg:col-span-3 flex flex-col gap-4\">\n    ${tid==='sql'?renderSqlOverview(tr):''}")
replace('recalcDateString(week.dateRange)','formatTrackWeek(tr,week)')
replace("recalcDateString(t.schedule||'')","formatTopicSchedule(tr,t)")
replace('recalcDateString(w.dateRange)','formatTrackWeek(tr,w)')
replace("recalcDateString(topic.schedule||'')","formatTopicSchedule(tr,topic)")
replace("  const sl=document.getElementById('m-subtopics-list'); sl.innerHTML='';", "  if(trackId==='sql') {\n    const sessionInfo=document.createElement('p');\n    sessionInfo.className='mt-2 text-cyan-300';\n    sessionInfo.textContent=topic.description;\n    why.appendChild(sessionInfo);\n  }\n  const sl=document.getElementById('m-subtopics-list'); sl.innerHTML='';")
replace("    // \"Término geral\" = data de fim da última trilha (maior endDate entre todas)\n    // storytelling e sql terminam por último (~77-82 dias após início)\n    // Usamos dsa.endDate ou testes.endDate como referência (ambos terminam ~mesmo dia)\n    const hubEnd = dates.dsa.endDate; // DSA é a trilha com maior duração", "    // Maior deslocamento entre as trilhas que acompanham o início do Hub.\n    const lastOffset = Math.max(...Object.values(TRACK_OFFSETS).map(o=>o.startOff+o.totalDays));\n    const hubEnd = fmtDateBR(addDaysToISO(startISO,lastOffset));")

helpers='''// SQL usa deslocamentos explícitos, sem interpretar datas antigas em texto.
function formatTrackWeek(tr, week) {
  if(tr.id!=='sql') return recalcDateString(week.dateRange);
  const first=hubDateFromOffset(week.startOffset);
  const last=hubDateFromOffset(week.startOffset+4);
  return first ? `${fmtDDMM(first)} a ${fmtDDMM(last)} · manhã` : week.dateRange;
}
function formatTopicSchedule(tr, topic) {
  if(tr.id!=='sql') return recalcDateString(topic.schedule||'');
  const date=hubDateFromOffset(topic.dayOffset);
  return date ? `${DIAS_PT_FULL[date.getDay()]}, ${fmtDDMM(date)} · manhã` : topic.schedule;
}
function renderSqlOverview(tr) {
  const dates=getEffectiveTrackDates('sql');
  const period=dates ? `${dates.startDate} → ${dates.endDate}` : 'Período definido ao iniciar o Hub';
  const sessions=tr.weeks.reduce((sum,w)=>sum+w.topics.length,0);
  return `<div class="bg-[#1e293b] border border-cyan-500/30 rounded-xl p-4">
    <h2 class="text-lg font-bold text-cyan-300">${tr.emoji} ${tr.title}</h2>
    <p class="text-sm font-bold text-slate-200 mt-1">${tr.source}</p>
    <p class="text-xs text-slate-400 mt-1">${tr.courseTitle}</p>
    <p class="text-[11px] mono text-cyan-300 mt-3">${tr.totalWeeks} semanas · ${sessions} sessões · ${trackTotal('sql')} subtópicos</p>
    <p class="text-[11px] mono text-slate-400 mt-1">${period} · ${tr.frequency}</p>
    <p class="text-xs text-slate-400 leading-relaxed mt-3">Reserve um bloco da manhã para SQL, separado do Inglês. Java Core/DSA/Testes seguem a partir das 13h; 19h–22h ficam para a Escola da Nuvem — Developer. Tempos estimados incluem aulas, comandos e prática curta. Retome pendências na ordem, sem dobrar a carga.</p>
    <p class="text-xs text-slate-400 leading-relaxed mt-2">Assista → execute os comandos → escreva algumas queries → revise erros → Feynman curto. Sábado: buffer, revisão leve ou descanso. Complementos SafeWallet são opcionais e não entram no progresso.</p>
    <div class="flex flex-wrap gap-3 text-[11px] text-cyan-300 mt-3">
      <a href="${tr.sourceUrl}" target="_blank" rel="noopener noreferrer" class="underline">1ª Rocketseat · fonte principal</a>
      <a href="https://sqlzoo.net/wiki/SQL_Tutorial" target="_blank" rel="noopener noreferrer" class="underline">2ª SQLZoo · complemento</a>
      <a href="https://www.hackerrank.com/domains/sql" target="_blank" rel="noopener noreferrer" class="underline">3ª HackerRank SQL · exercícios</a>
      <a href="https://www.postgresql.org/docs/" target="_blank" rel="noopener noreferrer" class="underline">4ª PostgreSQL Documentation · consulta opcional</a>
    </div>
    <p class="text-[10px] text-slate-500 leading-relaxed mt-3">Sessões agrupam conceitos do material e da descrição da jornada; seus títulos não representam nomes oficiais de vídeos. A descrição pública de Otimização e Performance repete Recursos Avançados do Postgres: siga a ordem real da plataforma nesses blocos. Progresso SQL anterior fica armazenado, mas não conclui automaticamente a nova jornada.</p>
  </div>`;
}

'''
replace('// -- Novas Trilhas ------------------------------------------------------------', helpers+'// -- Novas Trilhas ------------------------------------------------------------')
p.write_bytes(html.replace('\n','\r\n').encode('utf-8'))
print(json.dumps({'weeks':14,'sessions':len(sessions),'subtopics':sum(len(t['subtopics']) for w in track['weeks'] for t in w['topics']),'minutes':sum(s['minutes'] for s in sessions)},ensure_ascii=False))
