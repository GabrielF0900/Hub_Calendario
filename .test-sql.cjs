const fs = require('node:fs');
const vm = require('node:vm');
const assert = require('node:assert/strict');

const html = fs.readFileSync('index.html','utf8');
const code = [...html.matchAll(/<script\b[^>]*>([\s\S]*?)<\/script>/g)].map(match=>match[1]).filter(Boolean).join('\n');
new vm.Script(code);

const local = new Map();
const node = {textContent:'',innerHTML:'',style:{},classList:{add(){},remove(){},toggle(){}}};
const ctx = vm.createContext({
  Date,URLSearchParams,console,
  document:{addEventListener(){},getElementById(){return node;},querySelectorAll(){return[];},documentElement:{style:{setProperty(){}}}},
  window:{history:{replaceState(){}},location:{search:'',pathname:'/'}},
  localStorage:{getItem:key=>local.get(key)||null,setItem:(key,value)=>local.set(key,value),removeItem:key=>local.delete(key)},
  confirm:()=>true,alert:()=>{},fetch:async()=>({ok:true,json:async()=>({})})
});
vm.runInContext(code,ctx);
const run = source=>vm.runInContext(source,ctx);
const sql = JSON.parse(run('JSON.stringify(NEW_TRACKS.sql)'));
const tests = JSON.parse(run('JSON.stringify(NEW_TRACKS.testes)'));

assert.equal(sql.weeks.length,13);
assert.equal(tests.weeks.length,11);
assert(sql.weeks.flatMap(week=>week.topics).every(topic=>topic.dayOffset>=0));
assert(tests.weeks.flatMap(week=>week.topics).every(topic=>topic.dayOffset%7===4));
assert(run("trackTotal('sql')")>=201);
assert(run("trackTotal('testes')")>=70);

const sqlText = JSON.stringify(sql);
for (const term of ['ACID','Lost Update','Dirty Read','Non-repeatable Read','Phantom Read','READ UNCOMMITTED','READ COMMITTED','REPEATABLE READ','SERIALIZABLE','SELECT ... FOR UPDATE','@Version','Deadlock','UNIQUE(event_id)','idempotency key','SafeWallet']) assert(sqlText.includes(term),term);

const testText = JSON.stringify(tests);
for (const term of ['@DataJpaTest','@SpringBootTest','PostgreSQL','Testcontainers','rollback','Concorrencia no SafeWallet','JaCoCo','coverage != qualidade']) assert(testText.includes(term),term);

local.set('hub_startedAt','2026-09-14');
for (const topic of sql.weeks.flatMap(week=>week.topics)) assert([1,2,3,4,5].includes(run(`hubDateFromOffset(${topic.dayOffset}).getDay()`)));
for (const topic of tests.weeks.flatMap(week=>week.topics)) assert.equal(run(`hubDateFromOffset(${topic.dayOffset}).getDay()`),5);

console.log('PASS: SQL/Testes V4 — concorrencia, isolamento, locks, idempotencia, PostgreSQL real, Testcontainers e datas.');
