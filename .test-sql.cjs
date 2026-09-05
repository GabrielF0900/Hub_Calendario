const fs=require('node:fs');
const vm=require('node:vm');
const assert=require('node:assert/strict');
const path=require('node:path');
const before=fs.readFileSync(path.join(process.env.TEMP,'hub-sql-before.html'),'utf8');
const after=fs.readFileSync('index.html','utf8');
const scripts=h=>[...h.matchAll(/<script\b[^>]*>([\s\S]*?)<\/script>/g)].map(m=>m[1]).filter(s=>s.trim());
for(const code of scripts(after)) new vm.Script(code);
const data=h=>JSON.parse(h.slice(h.indexOf('const NEW_TRACKS = {')+19,h.indexOf('\n};',h.indexOf('const NEW_TRACKS = {'))+2));
const old=data(before),current=data(after);
for(const id of ['javacore','dsa','testes','storytelling']) assert.deepEqual(current[id],old[id],id);
const english=h=>h.slice(h.indexOf('const MD = ['),h.indexOf('const NEW_TRACKS = {'));
assert.equal(english(after),english(before),'English data/schedule unchanged');
const func=(h,start,end)=>h.slice(h.indexOf(start),h.indexOf(end,h.indexOf(start)));
assert.equal(func(after,'const SKEY =','function updateHeader('),func(before,'const SKEY =','function updateHeader('),'storage/progress/navigation unchanged');
assert.equal(func(after,'function iniciarHub()','function renderIniciarBanner('),func(before,'function iniciarHub()','function renderIniciarBanner('),'start/reset unchanged');
assert.equal(func(after,'function recalcDateString(','function previousMonday('),func(before,'function recalcDateString(','function previousMonday('),'legacy dates unchanged');
const seen=new Set();
for(const tr of Object.values(current)) for(const w of tr.weeks) for(const t of w.topics) {
  for(const o of [t,...t.subtopics||[]]) {assert(!seen.has(o.id),o.id);seen.add(o.id);}
}
const oldSqlIds=old.sql.weeks.flatMap(w=>w.topics.flatMap(t=>[t.id,...t.subtopics.map(s=>s.id)]));
for(const id of oldSqlIds) assert(!after.includes('"'+id+'"'),`Old SQL reference: ${id}`);
const tr=current.sql;
assert.equal(tr.totalWeeks,tr.weeks.length);
assert.equal(tr.weeks.length,14);
tr.weeks.forEach((w,i)=>{
  assert.equal(w.weekNum,i+1);assert.equal(w.startOffset,i*7);assert.equal(w.topics.length,5);
  w.topics.forEach((t,d)=>{
    assert.equal(t.dayOffset,i*7+d);assert(t.schedule.includes('manhã'));assert(!t.schedule.includes('13h'));
    assert(parseInt(t.estimatedTime)>=45 && parseInt(t.estimatedTime)<=90);
    assert(t.subtopics.length>0);
    t.subtopics.forEach(s=>{assert(s.id.startsWith('sql_rs_'));assert(['estudar','pratica','revisar'].includes(s.activityType));assert(!/Opcional:/.test(s.text));});
  });
});
const content=JSON.stringify(tr).toLowerCase();
const coverage=['introdução ao professor','tipos de bancos','bancos relacionais','sql','postgresql','beekeeper','create','insert','select','update','delete','numéricos','textuais','booleanos','uuid','seriais','array','json','entidade-relacionamento','entidades','atributos','relacionamentos','cardinalidade','primárias','estrangeiras','constraints','normalização','1fn','2fn','3fn','der','where','and','or','in','not in','between','like','distinct','order by','limit','count','sum','avg','max','min','group by','having','inner join','left join','right join','full join','subqueries','correlacionadas','cte','with','union','intersect','window functions','índices','planos de execução','explain','explain analyze','otimização','particionamento','denormalização','views','tabelas temporárias','funções','pl/pgsql','triggers','stored procedures','transactions','begin','commit','rollback','segurança','usuários','roles','permissões','grant','revoke','backup','restauração','mini projeto','gestão educacional','biblioteca universitária','big data','api','node.js','nosql','mongodb','tipos complexos','monitoramento','manutenção','tendências'];
for(const term of coverage) assert(content.includes(term),`Missing coverage: ${term}`);
// Run the real functions with in-memory localStorage, keeping onload/network inactive.
const local=new Map();
const context=vm.createContext({document:{addEventListener(){}},window:{},localStorage:{getItem:k=>local.get(k)||null,setItem:(k,v)=>local.set(k,v),removeItem:k=>local.delete(k)},Date,URLSearchParams,console});
vm.runInContext(scripts(after).join('\n'),context);
const run=code=>vm.runInContext(code,context);
assert.equal(run("trackTotal('sql')"),199);
run("setDone('sql_4_1a_1',true); setDone('jc_1_1_1',true)");
assert.equal(run("trackDone('sql')"),0);
assert.equal(run("trackDone('javacore')"),1);
for(const anchor of ['2026-09-07','2026-12-28','2028-02-28']) {
  local.set('hub_startedAt',anchor);
  assert.equal(run('hubDateFromOffset(0).getDay()'),1);
  assert.equal(run('hubDateFromOffset(95).getDay()'),5);
  assert.equal(run("getEffectiveTrackDates('sql').endDate"),run('fmtDateBR(addDaysToISO(getHubStartDate(),95))'));
  for(const id of ['javacore','dsa','testes','storytelling']) {
    const reference=vm.createContext({document:{addEventListener(){}},window:{},localStorage:{getItem:k=>local.get(k)||null},Date,URLSearchParams,console});
    vm.runInContext(scripts(before).join('\n'),reference);
    const expression=`JSON.stringify({dates:getEffectiveTrackDates('${id}'),weeks:NEW_TRACKS['${id}'].weeks.map(w=>({date:recalcDateString(w.dateRange),topics:w.topics.map(t=>recalcDateString(t.schedule))}))})`;
    assert.equal(run(expression),vm.runInContext(expression,reference),`${id} dynamic dates preserved`);
  }
}
console.log(JSON.stringify({syntax:'OK',otherTracks:'identical',ids:'unique; old SQL IDs absent',coverage:coverage.length,weeks:14,sessions:70,subtopics:199,dateAnchors:['2026-09-07','2026-12-28','2028-02-28']},null,2));
