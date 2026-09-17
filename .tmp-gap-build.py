import json
from pathlib import Path

p = Path('index.html')
h = p.read_text(encoding='utf8')
sessions = []
def s(key, module, title, study, practice, question, minutes=60, checkpoint=False):
    sessions.append(dict(key=key, module=module, title=title, study=study, practice=practice, question=question, minutes=minutes, checkpoint=checkpoint))

# 1–4: fundamentos, CRUD, modelagem e checkpoint (20 manhãs).
s('bancos',1,'Banco, tabela, registro e coluna','O que é um banco; importância; tipos de bancos; bancos relacionais; estrutura relacional; tabelas; linhas/registros e colunas','Desenhar uma tabela com dados de um sistema conhecido e explicar cada parte','Por que uma tabela tem colunas e vários registros?',45)
s('chaves',1,'PK, FK, SQL e PostgreSQL','Introdução a chaves; chave primária; chave estrangeira; introdução ao SQL; introdução ao PostgreSQL','Desenhar duas tabelas ligadas por PK/FK; distinguir linguagem SQL e PostgreSQL','Por que uma FK existe?',45)
s('ambiente',1,'Ambiente e primeiro banco','PostgreSQL e Beekeeper Studio: instalar/configurar somente se o ambiente não funcionar; caso já funcione, fazer revisão rápida de setup','Verificar conexão e criar um banco de estudo; aproveitar o tempo restante para reconhecer tabelas, registros, colunas, PK e FK','Qual a diferença entre SQL, PostgreSQL e Beekeeper Studio?',45)
s('create',2,'Estrutura, CREATE TABLE e tipos numéricos','Estrutura de uma tabela; CREATE TABLE; tipos numéricos','Criar uma tabela manualmente e justificar os tipos numéricos escolhidos','Por que escolher um tipo numérico adequado ao valor armazenado?')
s('tipos',2,'Texto, booleanos e datas','Tipos de texto; booleanos; datas/horários; escolha correta de tipos','Criar colunas de texto, booleano e data/hora; inserir valores de exemplo e conferir a representação','Quando data/hora é melhor que texto?')
s('constraints',2,'Constraints básicas','NOT NULL, UNIQUE, CHECK, DEFAULT e constraints básicas do módulo','Criar uma tabela com constraints e provocar uma violação para entender o erro','Qual regra o banco protege mesmo sem validação na API?')
s('insert_select',2,'INSERT e SELECT manual','INSERT; inserção de múltiplos registros; SELECT; seleção de colunas específicas; SELECT * e quando evitar','Inserir registros em lote e escrever consultas escolhendo explicitamente as colunas','Por que evitar SELECT * em uma consulta usada pela aplicação?')
s('update_delete',2,'UPDATE e DELETE com WHERE','UPDATE; UPDATE com WHERE; DELETE; DELETE com WHERE e cuidados','Em dados descartáveis, conferir o alvo com SELECT antes de alterar/excluir; comparar o resultado após cada comando','O que acontece se esquecer o WHERE em UPDATE ou DELETE?')
s('crud',2,'Prática de CRUD sem ORM','Concluir as 17 aulas e a atividade de Manipulação Básica de Dados, agrupadas nas sessões anteriores','Sem ORM e sem IA, escrever CREATE TABLE, INSERT, SELECT, UPDATE e DELETE; corrigir os erros e repetir sem copiar','Como provar que seu DELETE atingiu apenas os registros esperados?')
s('conceitual',3,'Por que modelar: entidades e atributos','Por que modelar; modelo conceitual; entidades; atributos; identificadores','Esboçar um modelo conceitual para empréstimos de livros','Como distinguir uma entidade de um atributo?')
s('relacoes',3,'Relacionamentos 1:1 e 1:N','Relacionamentos; relação 1:1; relação 1:N','Representar duas relações e justificar sua escolha sem anotações JPA','Onde fica a FK em uma relação 1:N?')
s('nn',3,'N:N e cardinalidade','Relacionamento N:N; cardinalidade','Modelar alunos e disciplinas com tabela associativa','Por que @ManyToMany não elimina a necessidade da tabela associativa?')
s('integridade',3,'Chaves e integridade referencial','Chave primária; chave estrangeira; integridade referencial','Implementar PK/FK e testar uma referência inexistente','Como a FK impede um registro órfão?')
s('der',3,'Modelo ER e DER','Modelo Entidade-Relacionamento; DER','Desenhar o DER do exemplo com atributos e cardinalidades','Como seu DER explica as relações que existem no banco?')
s('relacional',3,'Do conceitual ao relacional','Transformação do modelo conceitual em relacional','Converter o DER em tabelas PostgreSQL, incluindo a relação N:N','Qual tabela surgiu ao transformar o modelo N:N?')
s('normalizacao',3,'Redundância e normalização','Redundância; normalização; formas normais abordadas no curso, incluindo 1FN, 2FN e 3FN','Eliminar repetição e dependências inadequadas em um exemplo pequeno','Qual anomalia de atualização sua normalização evitou?')
s('modelagem_revisao',3,'Revisão de modelagem','Concluir as 20 aulas e a atividade de Modelagem de Dados Essencial; revisar somente lacunas','Normalizar e implementar um DER simples sem copiar o material','Por que este relacionamento existe no banco independentemente de @OneToMany ou @ManyToOne?')
s('educacional_modelo',4,'Mini projeto: sistema educacional','Aulas 1–2 do mini projeto: entender o sistema de gestão educacional; identificar entidades, atributos e relacionamentos','Construir o modelo e justificar cardinalidades','Como uma matrícula conecta aluno e turma?',75)
s('educacional_tabelas',4,'Mini projeto: implementar e explicar','Aula 3 do mini projeto: normalizar/modelar e implementar tabelas no PostgreSQL','Implementar tabelas, PK/FK e dados mínimos; revisão Feynman do modelo','Que inconsistência sua modelagem impede?',75)
s('checkpoint_fundamentos',4,'Checkpoint Nível 1 — fundamentos',None,'Faça sem consultar IA: criar banco/tabelas; definir PK/FK; escolher tipos; inserir, consultar, atualizar e excluir; desenhar DER; explicar cardinalidade e normalização básica. Concluir quiz de fundamentos. Se falhar, corrigir e revalidar antes de avançar','Por que suas PKs e FKs representam as regras do sistema?',75,True)
# 5–7: consultas, junções e desafio independente (15 manhãs).
s('where',5,'WHERE e filtros compostos','WHERE; operadores de comparação; AND; OR; NOT; filtros compostos','Escrever filtros com parênteses e conferir quais registros entram','Como os parênteses mudam um filtro com AND e OR?')
s('texto_intervalos',5,'Texto e intervalos','LIKE; filtros de texto; IN; BETWEEN','Criar consultas próprias para texto, lista de valores e período','Quais limites BETWEEN inclui?')
s('null_ordem',5,'NULL, ordenação e limites','NULL / IS NULL; ORDER BY; LIMIT quando abordado','Consultar dados ausentes e ordenar resultados com limite','Por que comparar uma coluna com NULL usando igualdade não funciona como IS NULL?')
s('agregadas',5,'Funções agregadas','Funções agregadas; COUNT; SUM; AVG','Calcular quantidade, total e média de transações de dados pequenos','Qual a diferença entre COUNT(*) e COUNT(coluna) quando há NULL?')
s('grupos',5,'GROUP BY e HAVING','GROUP BY; HAVING','Agrupar transações por tipo e filtrar os grupos resultantes','Qual a diferença entre WHERE e HAVING?')
s('join_intro',5,'Primeiro JOIN e revisão de consultas','Introdução/prática de JOIN do módulo; concluir as 20 aulas e a atividade de Consultas Avançadas','Relacionar duas tabelas; escrever um relatório com filtro, agregação e ordenação','Por que agregar depois de uma junção pode duplicar um total?')
s('inner',6,'P0 — INNER JOIN','Relacionamento entre múltiplas tabelas; INNER JOIN','Consultar usuário e carteira, conferindo cada par retornado','Quais linhas sem correspondência o INNER JOIN deixa de fora?')
s('left',6,'P0 — LEFT JOIN','LEFT JOIN','Comparar INNER JOIN e LEFT JOIN incluindo usuário sem carteira','Por que um LEFT JOIN pode retornar registros que um INNER JOIN não retorna?')
s('multi_join',6,'P0 — três tabelas e aliases','RIGHT JOIN e FULL JOIN quando presentes; JOIN com mais de duas tabelas; aliases','Priorizar um JOIN users + wallets + transactions; comparar brevemente RIGHT/FULL se apresentados','Como a cardinalidade explica o número de linhas de um JOIN de três tabelas?')
s('subquery',6,'P1 — subqueries','Subqueries; subqueries correlacionadas quando abordadas','Escrever uma subquery para comparar um valor com uma agregação','O que a consulta interna fornece à consulta externa?')
s('cte',6,'P1 — CTE / WITH','Common Table Expressions — CTE / WITH','Dividir uma consulta em etapas usando uma CTE básica','Como WITH torna as etapas da consulta mais claras?')
s('conjuntos',6,'Operações de conjunto','UNION; INTERSECT e operações de conjunto','Comparar união e interseção de dois resultados pequenos','Qual a diferença entre unir linhas e juntar colunas?')
s('window',6,'Window functions: introdução e revisão','Window functions introduzidas pelo curso; concluir as 12 aulas e atividade de Relacionamentos e Junções','Reproduzir uma única função de janela e comparar com GROUP BY; revisar JOINs como prioridade','Por que uma função de janela pode manter as linhas enquanto GROUP BY as agrupa?',45)
s('checkpoint_consultas_a',6,'Checkpoint Nível 2 — desafio sem ORM',None,'Faça sem consultar IA: em banco pequeno com users, wallets e transactions, consultar usuário + carteira, transações de uma carteira, total movimentado, número de transações e filtro por período. Escreva a query antes de conferir resposta','Como você conferiu o total sem depender de Hibernate?',75,True)
s('checkpoint_consultas_b',6,'Checkpoint Nível 2 — JOIN, subquery e CTE',None,'No mesmo banco: agrupamento por tipo, JOIN de três tabelas, uma subquery e uma CTE. Concluir quiz de consultas/modelagem. Validar resultados manualmente; corrigir lacunas antes do nível 3','Explique antes de abrir documentação: como a subquery e a CTE chegam ao resultado?',75,True)
# 8–10: apenas recursos úteis e consolidação pelo projeto oficial (15 manhãs).
s('indices',7,'Índices: benefício e custo','Conceito de índice; por que existe; criação/uso; quando ajuda; custo em escrita e armazenamento','Criar índice simples e comparar uma consulta com e sem ele','Quando um índice ajuda e qual custo ele adiciona?')
s('explain',7,'Plano de execução e EXPLAIN','Plano de execução; EXPLAIN; identificação de consulta lenta','Ler um plano básico e localizar scan/filtro; medir apenas em dados de estudo','Por que o PostgreSQL pode escolher não usar seu índice?')
s('otimizacao',7,'Otimização básica e modelagem','Otimização básica de queries; normalização versus denormalização','Melhorar uma consulta sem mudar seu resultado e justificar manter ou reduzir redundância','Qual custo de consistência a denormalização pode trazer?')
s('views','8/9','Views básicas','Views: conceito e uso básico; selecionar apenas a primeira ocorrência do assunto nos módulos 8/9','Criar e consultar uma view simples de relatório','Uma view comum armazena automaticamente o resultado?')
s('transacoes','8/9','Transações SQL e Spring','Transações; BEGIN; COMMIT; ROLLBACK; atomicidade; consistência; relação com @Transactional do Spring','Executar duas alterações como unidade; simular falha e ROLLBACK, depois sucesso e COMMIT; explicar o limite transacional no Spring','O que COMMIT e ROLLBACK fazem e qual unidade @Transactional deve proteger?',75)
s('permissoes','8/9','Segurança introdutória e revisão','Segurança/permissões introdutórias; princípio do menor privilégio; não repetir aulas equivalentes de 8/9','Em banco de estudo, verificar acesso restrito e revisar uma view, uma transação e um plano','Por que a conta da aplicação não precisa administrar o banco?')
s('final_contexto',10,'Projeto final: contexto e entidades','Sequência 1–2: Projeto Final Integrador — contexto e escopo; modelo conceitual — entidades e atributos','Usar o projeto oficial como consolidação; listar entidades e atributos sem criar outro grande projeto','Qual regra define cada entidade do projeto?',75)
s('final_der',10,'Projeto final: relações, DER e tabelas','Sequência 3–5: modelo conceitual — relacionamentos; DER; criando as tabelas','Implementar seu DER com tipos, PK/FK e constraints','Como cada FK corresponde a uma relação do DER?',90)
s('final_crud',10,'Projeto final: dados e CRUD','Sequência 6–7: inserindo dados; INSERT, UPDATE e DELETE','Escrever os comandos sem ORM e verificar alterações com SELECT','Como evitar alterar mais linhas que o necessário?',75)
s('final_filtros',10,'Projeto final: filtros complexos','Sequência 8–9: Filtros Complexos — partes 1 e 2','Criar filtros próprios sem copiar as respostas do curso','Como provar que um filtro composto inclui apenas o período solicitado?',75)
s('final_agregacao',10,'Projeto final: agregação e agrupamento','Sequência 10–11: funções de agregação; ordenação e agrupamento','Montar relatório com GROUP BY e HAVING e conferir totais','Por que seu HAVING não foi colocado no WHERE?',75)
s('final_joins',10,'Projeto final: junções e subconsultas','Sequência 12–13: junções; consultas avançadas e subconsultas','Escrever INNER JOIN, LEFT JOIN, JOIN múltiplo, subquery e CTE básica no projeto','Como a consulta preserva registros sem correspondência?',90)
s('final_performance',10,'Projeto final: performance e views','Sequência 14–15: otimização e performance; views','Analisar índice e EXPLAIN básico; criar uma view do relatório sem repetir toda a teoria','Qual evidência justifica seu índice?',75)
s('final_transacao',10,'Projeto final: transações e revisão','Sequência 16: na aula Stored Procedure/Transações, priorizar o trecho de transações; aula exclusiva de triggers/funções avançadas é opcional','Validar COMMIT/ROLLBACK no projeto e revisar consultas que ainda exigem copiar exemplos','Qual operação deve ser atômica e por quê?',75)
s('validacao_final',10,'Validação final — SQL para Backend Java',None,'Refazer consultas do projeto sem ORM e sem IA; explicar antes de abrir documentação. Só marcar cada competência abaixo após demonstrá-la. Se falhar, retomar a lacuna e repetir a validação na próxima manhã disponível','Como provar que você consegue escrever e explicar SQL sem depender de JPA?',90,True)
assert len(sessions)==50

sql_method='Assistir → executar o exemplo → fechar o exemplo → escrever outra query sem copiar → testar → corrigir erro → Feynman de 12 minutos. Explique cada query linha por linha. Nas revisões, use o tempo de vídeo para corrigir lacunas.'
sql=dict(id='sql',title='SQL + PostgreSQL',emoji='🗄️',order=5,totalWeeks=10,startDate='Ao iniciar o Hub',endDate='Sexta da semana 10',color='#06b6d4',frequency='Segunda a sexta · manhã · 08h30 · 45–60 min (75–90 min em práticas)',source='Rocketseat — Banco de Dados',courseTitle='Banco de dados, na prática: do básico ao avançado com PostgreSQL',sourceUrl='https://app.rocketseat.com.br/jornada/banco-de-dados/conteudos',objective='SQL/PostgreSQL para Backend Java',whyStudy='Escrever e explicar SQL manualmente, compreender o banco além de Prisma/JPA/Hibernate e sustentar decisões de Backend Java Júnior. Fundamentos → prática → aplicação → revisão → validação.',feynmanPractice=sql_method,method=sql_method,weeks=[],optionalSections=[
 dict(title='Depois do gap / conteúdos avançados opcionais',items=['Opcional, fora do progresso: introdução do professor.','P2 / depois: particionamento; tabelas temporárias; views avançadas; administração de usuários/permissões.','Parking Lot: PL/pgSQL profundo; funções, triggers e stored procedures avançadas; particionamento avançado; administração avançada; backup/restauração operacional aprofundado.','Módulo 11, fora do gap: Big Data, integração banco + API e CRUD por API em Node.js, MongoDB/NoSQL ficam no Parking Lot; JSON/tipos complexos e monitoramento/manutenção ficam P2; tendências são opcionais.']),
 dict(title='SafeWallet — laboratório complementar opcional',items=['Após o checkpoint de fundamentos: observar tabelas geradas pelo Hibernate, identificar PK/FK e escrever SELECT manual.','Após JOINs: consultar histórico, juntar tabelas reais e realizar agregações.','Após índices/transações: observar queries geradas pelo Hibernate, criar/analisar índice simples, executar EXPLAIN e relacionar transação SQL a @Transactional.','Limite sugerido: 15 minutos dentro do bloco disponível, só se a prática principal estiver concluída; sem nova sessão fixa ou novo projeto. Não conta no progresso.'])])
sql_criteria=['Criar tabelas','Usar PK/FK','Fazer CRUD manual','Escrever SELECT','Escrever filtros','Usar agregações','Usar GROUP BY/HAVING','Usar INNER JOIN','Usar LEFT JOIN','Fazer JOIN de múltiplas tabelas','Escrever subquery','Escrever CTE básica','Explicar normalização','Entender índices','Ler EXPLAIN básico','Entender transações','Resolver consultas sem ORM']
for i,x in enumerate(sessions):
    wi,di=divmod(i,5)
    if di==0: sql['weeks'].append(dict(weekNum=wi+1,startOffset=wi*7,dateRange=f'Semana {wi+1} · segunda a sexta · manhã',isReviewWeek=False,topics=[]))
    key='sql_jr_v2_'+x['key']; mins=x['minutes']; pause=5 if mins>=75 else 0
    subs=[]
    if x['study']: subs.append(dict(id=key+'_estudo',text=x['study'],activityType='estudar'))
    subs.append(dict(id=key+'_pratica',text=x['practice'],activityType='pratica'))
    subs.append(dict(id=key+'_feynman',text='Feynman (12 min), sem IA: '+x['question'],activityType='revisar'))
    if x['key']=='validacao_final':
        subs += [dict(id=key+'_competencia_'+str(n+1),text='Demonstrar sem IA: '+v,activityType='revisar') for n,v in enumerate(sql_criteria)]
    end=8*60+30+mins
    sql['weeks'][-1]['topics'].append(dict(id=key,title=x['title'],dayOffset=wi*7+di,schedule=['Segunda','Terça','Quarta','Quinta','Sexta'][di]+f' · manhã · 08h30–{end//60:02}h{end%60:02}',timeSlot=f'08h30–{end//60:02}h{end%60:02}',estimatedTime=f'{mins} minutos',durationMinutes=mins,breakMinutes=pause,activityType='revisar' if x['checkpoint'] else 'pratica' if mins>=75 else 'estudar',checkpoint=x['checkpoint'],block='Módulo '+str(x['module']),priority='P1' if x['key'] in ['subquery','cte','conjuntos','window'] else 'P0',description=f"Rocketseat · módulo {x['module']}. "+('Validação obrigatória: demonstre antes de marcar; só avance após corrigir as lacunas. ' if x['checkpoint'] else 'Estude os conceitos agrupados e pratique sem ORM. ')+f"Bloco de {mins} min, incluindo 12 min de Feynman"+(' e pausa de 5 min no meio.' if pause else '.')+' Faça uma pausa de pelo menos 15 min antes do Inglês; reserve almoço/descanso antes das 13h.',feynmanPractice=x['question']+' Explique sem IA antes de abrir documentação.',subtopics=subs))

lessons=[
'O que são testes em uma aplicação? — por que testar; unit test vs integration test',
'Criando primeiro teste unitário — JUnit 5, @Test, assertions, assertEquals, assertTrue e Arrange / Act / Assert (AAA)',
'ApplyJobCandidate — testes do UseCase e comportamento esperado',
'Testes das regras de negócio — happy path e invariantes',
'Cenários de exceção — error path e assertThrows',
'Testes de validações — entradas inválidas e limites',
'Preparação/criação das entidades necessárias aos cenários — dados mínimos e isolamento',
'Testes com dependências/mocks — Mockito, @Mock, quando substituir dependência, when(...).thenReturn(...) e verify(...)',
'JobController — preparação dos testes e limites entre camadas',
'JobController — cenário principal',
'JobController — validações',
'JobController — erros/exceções',
'JobController — integração/fluxos apresentados no curso',
'Quiz/checkpoint do bloco Testes da Aplicação']
test_method='Assistir → reproduzir → escrever teste sem copiar → explicar o teste antes de rodá-lo → rodar → forçar cenário de erro → explicar o que o teste garante. Faça sem consultar IA nos checkpoints.'
tests=dict(id='testes',title='Testes',emoji='✅',order=4,totalWeeks=8,startDate='Ao iniciar o Hub',endDate='Sexta da semana 8',color='#3b82f6',frequency='Sexta-feira · 13h–15h · pausa 13h50–14h',source='Rocketseat — Formação Java — Testes e Qualidade de Código',courseTitle='Testes da Aplicação completo + JaCoCo',sourceUrl='https://app.rocketseat.com.br/classroom/testes-e-qualidade-de-codigo',objective='JUnit + Mockito + testes de aplicações Spring',whyStudy='Criar, rodar e explicar testes Java/Spring que protegem comportamentos reais do SafeWallet. Aprender JUnit e Mockito com aplicação progressiva, antes de concluir toda a teoria.',feynmanPractice=test_method,method=test_method,weeks=[],optionalSections=[dict(title='Próximos passos — fora do progresso principal',items=['Qualidade de Código / Refatoração: P1/P2, aplicar pontualmente aos testes existentes; quiz de qualidade opcional.','Parking Lot: Configurando SonarQube; Configurando Projeto Sonar; Quality Gate / QG Overall.','Depois, conforme necessidade: Mockito avançado; BDDMockito; @Spy avançado; ArgumentCaptor avançado; mutation testing; TDD aprofundado; testes parametrizados. Nenhuma semana extra reservada para esses assuntos.'])])
test_rows=[
('junit','Fundamentos + primeiro JUnit',[1,2],['Reproduzir o primeiro teste, fechar o exemplo e escrever um teste JUnit próprio com @Test, assertEquals, assertTrue e AAA; executar e provocar uma falha controlada.'],'Qual diferença entre teste unitário e de integração?', '40 min de aulas/reprodução + 55 min de prática + 15 min de explicação'),
('regras','JUnit e regras de negócio',[3,4,5,6],['SafeWallet — etapa A: testar uma regra real com comportamento esperado e valor inválido ou saldo insuficiente; usar assertThrows para a exceção esperada. Não copiar código pronto.'],'Por que testar somente happy path é insuficiente?', '45 min de aulas/reprodução + 50 min de prática + 15 min de explicação'),
('mockito','Mockito e dependências',[7,8],['SafeWallet — etapa B: criar @Mock para Repository de um Service; configurar when(...).thenReturn(...); rodar happy path e verificar interação relevante com verify(...).'],'Por que eu mockei o Repository e o que verify() está garantindo?', '40 min de aulas/reprodução + 55 min de prática + 15 min de explicação'),
('service','Service: sucesso, erro e independência',[],['Sem IA: completar no mesmo Service um happy path e um error path; verificar resultado/exceção e uma interação relevante (inclusive ausência de gravação em entrada inválida).','Alterar temporariamente a regra protegida, observar o teste falhar, restaurar e rodar novamente; explicar o teste antes de rodá-lo.'],'Se eu alterar esse Service, qual comportamento este teste protege?', '20 min de revisão + 75 min de prática + 15 min de explicação'),
('controller','Controller: preparação, sucesso e validações',[9,10,11],['Registrar nas anotações a ferramenta/anotações Spring efetivamente usadas no curso; reproduzir a configuração. O material local não confirma se usa MockMvc ou outra ferramenta; não presumir título nem stack.','Identificar o limite do teste de controller e o que é simulado; reproduzir requisição/status/corpo e validações conforme a aula.'],'Quais camadas seu teste de controller realmente executa?', '50 min de aulas/reprodução + 45 min de prática + 15 min de explicação'),
('integracao','Controller: erros, integração e quiz',[12,13,14],['Reproduzir erros/exceções e os fluxos de integração apresentados; identificar dependências reais e substituídas.','SafeWallet — etapa C: adaptar um teste de controller/fluxo HTTP conforme aprendido; distinguir integração entre camadas de uma cadeia inteiramente mockada.'],'Por que mockar todas as camadas não demonstra a integração real?', '50 min de aulas/quiz + 45 min de prática + 15 min de explicação'),
('jacoco','SafeWallet: testes reais e JaCoCo',[],['Consolidar no SafeWallet um teste de controller e os testes reais de Service com sucesso/erro; rodar a suíte.','Rocketseat — Configurando JaCoCo: estudar e configurar depois de existirem testes reais; gerar e ler relatório de cobertura.','Cobertura mede código executado pelos testes; não mede automaticamente qualidade dos testes. Identificar um comportamento relevante ausente, sem meta artificial de 100%.'],'Como um teste pode executar uma linha sem garantir seu comportamento?', '30 min de JaCoCo/reprodução + 65 min de prática + 15 min de explicação'),
('validacao','Revisão + simulado Feynman + validação',[],['Faça sem consultar IA: escrever ou reconstruir um teste de regra do SafeWallet, rodar sucesso e erro e explicar o comportamento protegido.','Revisar os erros, rodar a suíte real e conferir seu relatório JaCoCo; manter os testes no repositório do SafeWallet e registrar como executá-los.','Só marcar as competências abaixo após demonstrá-las; se não conseguir, repetir a lacuna na próxima sexta às 13h, sem nova tarde fixa.'],'O que seus testes garantem, o que não garantem e qual regressão detectariam?', '20 min de revisão + 65 min de prática/validação + 25 min de simulado Feynman')]
test_criteria=['Explicar unit vs integration test','Criar teste JUnit','Usar assertions','Usar assertThrows','Estruturar AAA','Testar happy path','Testar error path','Criar mock','Configurar retorno de mock','Verificar interação','Testar Service','Compreender teste de Controller','Possuir testes reais no SafeWallet','Explicar os testes sem consultar IA','Compreender cobertura com JaCoCo']
for wi,(key,title,nums,practices,q,budget) in enumerate(test_rows):
    key='tst_jr_v2_'+key
    subs=[dict(id='tst_jr_v2_aula_'+str(n).zfill(2),text=f'Rocketseat — item {n}/14: '+lessons[n-1],activityType='estudar',courseOrder=n) for n in nums]
    subs += [dict(id=key+'_pratica_'+str(n+1),text=v,activityType='pratica') for n,v in enumerate(practices)]
    subs.append(dict(id=key+'_feynman',text='Feynman, sem IA: '+q,activityType='revisar'))
    if wi==7: subs += [dict(id=key+'_competencia_'+str(n+1),text='Demonstrar sem IA: '+v,activityType='revisar') for n,v in enumerate(test_criteria)]
    topic=dict(id=key,title=title,dayOffset=wi*7+4,schedule='Sexta · 13h–15h',timeSlot='13h–15h',durationMinutes=120,breakMinutes=10,estimatedTime='120 minutos · pausa de 10 min incluída',activityType='revisar' if wi==7 else 'pratica' if wi in [3,6] else 'estudar',checkpoint=wi in [3,7],block='Testes da Aplicação' if wi<6 else 'Qualidade / validação',description=budget+'. Pausa fixa 13h50–14h; total de 110 min de estudo em 2h. Títulos descritivos; seguir a ordem oficial do bloco, sem omitir seus 14 itens.',feynmanPractice=q+' Explique o teste antes de rodá-lo.',subtopics=subs)
    tests['weeks'].append(dict(weekNum=wi+1,startOffset=wi*7+4,dateRange=f'Semana {wi+1} · sexta · 13h–15h',isReviewWeek=wi==7,topics=[topic]))

for name,tr,nextname in [('sql',sql,'storytelling'),('testes',tests,'sql')]:
    start=h.index('  "'+name+'": {'); end=h.index('  "'+nextname+'": {',start)
    h=h[:start]+'  "'+name+'": '+json.dumps(tr,ensure_ascii=False,indent=2).replace('\n','\n  ')+',\n'+h[end:]

def replace(old,new):
    global h
    assert old in h,old[:100]
    h=h.replace(old,new)

replace('Sex 07/08/2026</div>','<span id="testesEntryDate">Sexta da semana 1</span></div>')
replace("  const mc=document.getElementById('mainContainer');", "  const testsEntry=document.getElementById('testesEntryDate');\n  if(testsEntry) testsEntry.textContent=getHubStartDate() ? 'Sex '+getEffectiveTrackDates('testes').startDate : 'Sexta da semana 1';\n  const mc=document.getElementById('mainContainer');")
replace("testes:       { startOff: 4,  totalDays: 79 },  // 07/08 → 25/10 = 79 dias", "testes:       { startOff: 4,  totalDays: NEW_TRACKS.testes.weeks.at(-1).topics.at(-1).dayOffset - 4 }, // Sexta da S1 até sexta final")
replace("if(tr.id!=='sql') return recalcDateString(week.dateRange);", "if(tr.id!=='sql' && tr.id!=='testes') return recalcDateString(week.dateRange);\n  if(tr.id==='testes') return formatTopicSchedule(tr,week.topics[0]);")
replace("if(tr.id!=='sql') return recalcDateString(topic.schedule||'');", "if(tr.id!=='sql' && tr.id!=='testes') return recalcDateString(topic.schedule||'');")
replace("return date ? `${DIAS_PT_FULL[date.getDay()]}, ${fmtDDMM(date)} · manhã` : topic.schedule;", "return date ? `${DIAS_PT_FULL[date.getDay()]}, ${fmtDDMM(date)} · ${tr.id==='sql'?'manhã · ':''}${topic.timeSlot}` : topic.schedule;")
start=h.index('function renderSqlOverview(tr) {'); end=h.index('// -- Novas Trilhas',start)
h=h[:start]+'''function renderGapOverview(tr) {
  const dates=getEffectiveTrackDates(tr.id);
  const topics=tr.weeks.flatMap(w=>w.topics);
  const minutes=topics.reduce((sum,t)=>sum+t.durationMinutes,0);
  const weekMinutes=tr.weeks.map(w=>w.topics.reduce((sum,t)=>sum+t.durationMinutes,0));
  const hours=n=>(n/60).toLocaleString('pt-BR',{maximumFractionDigits:2});
  const period=dates ? `${dates.startDate} → ${dates.endDate}` : 'Datas definidas ao iniciar o Hub';
  const optional=tr.optionalSections.map(section=>`<details class="mt-3 border-t border-slate-700 pt-3"><summary class="cursor-pointer font-bold text-slate-300">${section.title}</summary><ul class="list-disc pl-5 mt-2 space-y-2">${section.items.map(item=>`<li>${item}</li>`).join('')}</ul></details>`).join('');
  return `<section class="bg-[#1e293b] border border-slate-600 rounded-xl p-4 text-xs text-slate-400 leading-relaxed">
    <h2 class="text-lg font-bold" style="color:${tr.color}">${tr.emoji} ${tr.title}</h2>
    <p class="text-sm font-bold text-slate-200 mt-2">Fonte principal: ${tr.source}</p>
    <p>${tr.courseTitle}</p>
    <p class="font-bold text-slate-200 mt-2">Objetivo: ${tr.objective}</p>
    <p class="mono mt-3">${tr.totalWeeks} semanas · ${topics.length} sessões · ${trackTotal(tr.id)} subtópicos · ${hours(minutes)}h de blocos no total</p>
    <p class="mono">${hours(Math.min(...weekMinutes))}–${hours(Math.max(...weekMinutes))}h/semana · média ${hours(minutes/tr.totalWeeks)}h · pausas internas incluídas</p>
    <p class="mt-2">${period} · ${tr.frequency}</p>
    <p class="mt-3">SQL de manhã, separado do Inglês por pelo menos 15 min de descanso. Reserve almoço/descanso antes das 13h. Java Core/DSA nos calendários existentes; Testes somente sexta, 13h–15h, com pausa 13h50–14h. Segunda a sexta, 19h–22h: Escola da Nuvem — Developer, horário fixo e exclusivo.</p>
    <p class="mt-2">${tr.method}</p>
    <p class="mt-2">Fundamentos → prática → aplicação → revisão → validação. O check-in registra presença; os subtópicos registram prática demonstrada. Os checkpoints são obrigatórios e não são concluídos pela passagem das datas. Corrija lacunas antes de avançar, sem empilhar blocos.</p>
    <p class="mt-2">${tr.id==='sql'?'Módulos 1–6: estudar o conteúdo selecionado completo (apresentação do professor opcional e setup condicional). Módulo 7: índices, EXPLAIN e otimização básica. Módulos 8/9: somente views, transações e segurança introdutória, sem duplicar aulas equivalentes. Módulo 10: consolidação na sequência descrita.':'Os 14 itens de Testes da Aplicação estão distribuídos na ordem informada, com prática no SafeWallet desde a semana 2. Os nomes são descrições pedagógicas quando o título oficial completo não está disponível.'}</p>
    <p class="mt-2">Tempos estimados incluem prática e revisão, não são durações oficiais de vídeos. ${tr.id==='sql'?'A grade pública informa 12h33 de vídeo nos módulos 1–6 e 3h22 no projeto completo; o recorte avançado e o projeto são filtrados. Os blocos reservam tempo adicional para escrever SQL.':'A duração exata dos 14 itens não está disponível no projeto nem foi confirmada publicamente; 8 semanas reservam 16h, sendo 14h40 de estudo e 1h20 de pausas. Se necessário, retome na próxima sexta mantendo a ordem.'}</p>
    <a href="${tr.sourceUrl}" target="_blank" rel="noopener noreferrer" class="inline-block underline mt-3" style="color:${tr.color}">Abrir fonte principal — Rocketseat</a>
    <p class="mt-3">Progresso anterior de SQL e Testes permanece salvo, mas não marca automaticamente estas novas competências. Revalide o que já domina. Java Core, DSA, Inglês e Storytelling mantêm seus IDs e progresso.</p>
    ${optional}
  </section>`;
}

'''+h[end:]
replace("${tid==='sql'?renderSqlOverview(tr):''}","${tid==='sql'||tid==='testes'?renderGapOverview(tr):''}")
replace("if(trackId==='sql') {", "if(trackId==='sql'||trackId==='testes') {")
replace("document.getElementById('m-feynman-text').textContent=tr.feynmanPractice;", "document.getElementById('m-feynman-text').textContent=topic.feynmanPractice||tr.feynmanPractice;")
# Checkpoints keep their individual checkboxes; bulk completion must not skip validation.
replace("onclick=\"event.stopPropagation();qToggleNew('${t.id}','${tr.id}')\"", "onclick=\"event.stopPropagation();${t.checkpoint?`openTrackModal('${tr.id}','${t.id}')`:`qToggleNew('${t.id}','${tr.id}')`}\"")
replace("${comp?'&#x2705; Conclu&#237;do':'&#x25CB; Completar Todos os Sub-t&#243;picos'}", "${t.checkpoint?'Validar competências individualmente':comp?'&#x2705; Conclu&#237;do':'&#x25CB; Completar Todos os Sub-t&#243;picos'}")
replace("  if(!topic) return;\n  let tot=", "  if(!topic) return;\n  if(topic.checkpoint){openTrackModal(trackId,tid);return;}\n  let tot=")
replace('SQL — Feynman: Depois de escrever uma query, explique em voz alta linha por linha o que ela faz. Se não souber explicar uma cláusula, revise apenas aquela parte.', 'SQL: assistir → executar exemplo → escrever query própria sem copiar → testar → corrigir → Feynman de 12 minutos. Testes: assistir → reproduzir → escrever teste sem copiar → rodar → forçar erro → explicar o que garante. Checkpoints sem IA; explique antes de abrir documentação.')
p.write_bytes(h.replace('\n','\r\n').encode('utf8'))
print(json.dumps({tr['id']:{'weeks':tr['totalWeeks'],'sessions':sum(len(w['topics']) for w in tr['weeks']),'minutes':sum(t['durationMinutes'] for w in tr['weeks'] for t in w['topics']),'subtopics':sum(len(t['subtopics']) for w in tr['weeks'] for t in w['topics'])} for tr in [sql,tests]}))
