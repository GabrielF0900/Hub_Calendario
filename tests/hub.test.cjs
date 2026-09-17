const fs = require('node:fs');
const vm = require('node:vm');
const assert = require('node:assert/strict');
const path = require('node:path');

const root = path.resolve(__dirname, '..');
const html = fs.readFileSync(path.join(root, 'index.html'), 'utf8');
const code = [...html.matchAll(/<script\b[^>]*>([\s\S]*?)<\/script>/g)].map(match=>match[1]).filter(Boolean).join('\n');
new vm.Script(code);

function context(source = code) {
  const local = new Map();
  const nodes = new Map();
  const node = id => {
    if (!nodes.has(id)) nodes.set(id, {textContent:'',innerHTML:'',style:{},classList:{add(){},remove(){},toggle(){}}});
    return nodes.get(id);
  };
  const ctx = vm.createContext({
    Date, URLSearchParams, console,
    document:{addEventListener(){},getElementById:node,querySelectorAll(){return[];},documentElement:{style:{setProperty(){}}}},
    window:{history:{replaceState(){}},location:{search:'',pathname:'/'}},
    localStorage:{getItem:key=>local.get(key)||null,setItem:(key,value)=>local.set(key,value),removeItem:key=>local.delete(key)},
    confirm:()=>true, alert:()=>{}, fetch:async()=>({ok:true,json:async()=>({})})
  });
  vm.runInContext(source, ctx);
  return {local,nodes,run:text=>vm.runInContext(text,ctx)};
}

const {local,nodes,run} = context();
const tracks = JSON.parse(run('JSON.stringify(NEW_TRACKS)'));
const english = JSON.parse(run('JSON.stringify(ALL)'));
assert.equal(english.length,225,'English must keep 225 lessons');
assert.equal(run('SKEY'),'hubGabrielV3');
assert.equal(run('HUB_START_KEY'),'hub_startedAt');

const ids = new Set(english.map(lesson=>lesson.id));
for (const track of Object.values(tracks)) for (const week of track.weeks) for (const topic of week.topics) {
  for (const item of [topic,...topic.subtopics||[]]) {
    assert(!ids.has(item.id),`Duplicate ID: ${item.id}`);
    ids.add(item.id);
  }
}

const staticIds = [...html.matchAll(/\bid="([^"]+)"/g)].map(match=>match[1]);
assert.equal(new Set(staticIds).size,staticIds.length,'Static HTML IDs must be unique');
assert.deepEqual(Object.keys(tracks),['javacore','dsa','testes','sql','storytelling','systemdesign','mockinterview']);
assert.equal(tracks.sql.weeks.length,13);
assert.equal(tracks.testes.weeks.length,11);
assert.equal(tracks.systemdesign.weeks.length,8);
assert.equal(tracks.mockinterview.weeks.length,6);

for (const track of Object.values(tracks)) {
  assert.equal(track.totalWeeks,track.weeks.length,`${track.id} totalWeeks`);
  assert.equal(new Set(track.weeks.map(week=>week.weekNum)).size,track.weeks.length,`${track.id} week numbers`);
  track.weeks.forEach(week=>{
    for (const topic of week.topics) {
      assert(topic.id && topic.title && topic.estimatedTime,`${track.id} topic schema`);
      assert(Array.isArray(topic.subtopics) && topic.subtopics.length,`${topic.id} subtopics`);
      assert.equal(topic.subtopics.length,new Set(topic.subtopics.map(item=>item.id)).size,`${topic.id} subtopic IDs`);
    }
  });
}

const corpus = JSON.stringify(tracks);
for (const term of ['Lost Update','READ COMMITTED','SELECT ... FOR UPDATE','@Version','Deadlock','UNIQUE(event_id)','Testcontainers','@DataJpaTest','@SpringBootTest','idempotency key']) assert(corpus.includes(term),term);
for (const term of ['Webhook at-least-once','Antifraude lento','Notificacoes','Upload de arquivos','Pedidos + pagamento + estoque','Rate Limiting','Cache','Sistema final']) assert(corpus.includes(term),term);
for (const id of ['javacore','dsa','testes','sql','storytelling','systemdesign','mockinterview']) assert(run(`trackTotal('${id}')`)>0,id);

run("setDone('sql_rs_01_01',true); setDone('tst_3_1_1',true); setDone('jc_1_1_1',true); setDone('dsa_2_1_1',true); setDone('sty_5_1_1',true); setDone('m1l1',true)");
for (const id of ['javacore','dsa','storytelling','ingles']) assert.equal(run(`trackDone('${id}')`),1,`${id} legacy progress`);
assert(run("isDone('sql_rs_01_01') && isDone('tst_3_1_1')"),'Legacy records retained even when not mapped to new curricula');
const protectedProgress = local.get('hubGabrielV3');

for (const anchor of ['2026-09-14','2026-12-28','2028-02-28']) {
  local.set('hub_startedAt',anchor);
  for (const id of ['sql','testes']) for (const topic of tracks[id].weeks.flatMap(week=>week.topics)) {
    const dow = run(`hubDateFromOffset(${topic.dayOffset}).getDay()`);
    assert(id==='sql'?dow>=1&&dow<=5:dow===5,`${id} weekday`);
    const schedule = run(`formatTopicSchedule(NEW_TRACKS.${id},NEW_TRACKS.${id}.weeks.flatMap(w=>w.topics).find(t=>t.id==='${topic.id}'))`);
    assert(schedule.includes(topic.timeSlot),`${topic.id} schedule`);
  }
}

run('renderMain=()=>{}; updateHeader=()=>{}');
run('resetHub()');
assert(!local.has('hub_startedAt'));
assert.equal(local.get('hubGabrielV3'),protectedProgress,'Reset date preserves progress');
run('iniciarHub()');
assert.equal(run('hubDateFromOffset(0).getDay()'),1,'Hub starts on Monday');
assert.equal(local.get('hubGabrielV3'),protectedProgress,'Starting preserves progress');
run("addStudyLog('sql');addStudyLog('sql');addStudyLog('testes')");
assert.equal(run('getStudyLog().length'),2,'Duplicate check-ins prevented');
assert.equal(local.get('hubGabrielV3'),protectedProgress,'Check-in does not alter completion');

run("NEW_TRACKS.sql.weeks.forEach(w=>w.topics.forEach(t=>t.subtopics.forEach(s=>setDone(s.id,true))))");
assert.equal(run("trackDone('sql')"),run("trackTotal('sql')"));
run("activeTab='sql';updateProgress()");
assert.equal(nodes.get('pt-pct').textContent,'(100%)');
const total = Number(nodes.get('pg-text').textContent.split(' de ')[1]);
assert.equal(total,run("['ingles','javacore','dsa','testes','sql','storytelling','systemdesign','mockinterview'].reduce((sum,id)=>sum+trackTotal(id),0)"));

const reloaded = context();
for (const [key,value] of local) reloaded.local.set(key,value);
assert.equal(reloaded.run("trackDone('sql')"),run("trackTotal('sql')"),'Persistence after reload');

console.log('PASS: syntax, unique IDs, 225 English lessons, V4 tracks, competency content, legacy storage, dates, check-ins and global progress.');
console.log(JSON.stringify(Object.fromEntries(['sql','testes','systemdesign','mockinterview'].map(id=>[id,{weeks:tracks[id].weeks.length,subtopics:run(`trackTotal('${id}')`)}])),null,2));
