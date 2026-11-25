// Model only local browser events. No real form submission or network access.
const assert = require('node:assert/strict');
const fs = require('node:fs');
const vm = require('node:vm');
const { webcrypto } = require('node:crypto');
const script = fs.readFileSync(require('node:path').join(__dirname,'../feedback.js'),'utf8');
function setup(configured) {
  const handlers={}, windowHandlers={}, fields={reference:{value:''},_next:{value:'https://hoplontec.io/nivilog-feedback-thanks.html'}};
  const button={textContent:'Send feedback',disabled:false};
  const form={dataset:{configured:String(configured),next:fields._next.value,pending:'Sending…'},
    elements:{namedItem:name=>fields[name]},querySelector:()=>button,
    addEventListener:(name,fn)=>handlers[name]=fn,setAttribute(){},removeAttribute(){}};
  vm.runInNewContext(script,{document:{querySelector:s=>s==='#feedback-form'?form:null},window:{addEventListener:(name,fn)=>windowHandlers[name]=fn},crypto:webcrypto});
  return {handlers,windowHandlers,fields,button};
}
const unavailable=setup(false);let stopped=0;
unavailable.handlers.submit({preventDefault(){stopped++;}});assert.equal(stopped,1);assert.equal(unavailable.fields.reference.value,'');
const active=setup(true);active.handlers.submit({preventDefault(){throw Error('unexpected block');}});
assert.match(active.fields.reference.value,/^[a-f0-9]{32}$/);assert.equal(active.fields._next.value,`https://hoplontec.io/nivilog-feedback-thanks.html#reference=${active.fields.reference.value}`);
assert.equal(active.button.disabled,true);active.handlers.submit({preventDefault(){stopped++;}});assert.equal(stopped,2);
active.windowHandlers.pageshow();assert.equal(active.button.disabled,false);assert.equal(active.button.textContent,'Send feedback');
console.log('Feedback events: unavailable guard, reference, double-click prevention and Back recovery passed.');
