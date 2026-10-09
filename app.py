from flask import Flask, render_template_string

app = Flask(__name__)

PAGE = r"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>A tiny question for you 💗</title>
<style>
:root{--pink:#ff7da8;--deep:#d94f82;--cream:#fff8f7;--ink:#60384b;--mint:#e7f8ee}
*{box-sizing:border-box}
body{margin:0;min-height:100vh;font-family:'Trebuchet MS',system-ui,sans-serif;color:var(--ink);
background:radial-gradient(circle at top left,#ffe0eb,transparent 38%),linear-gradient(135deg,#fff8f7,#fff0f5);
overflow-x:hidden}
.heart{position:fixed;bottom:-30px;opacity:.45;animation:floatUp 9s linear infinite;pointer-events:none;z-index:0}
@keyframes floatUp{to{transform:translateY(-115vh) rotate(25deg);opacity:0}}
main{position:relative;z-index:1;max-width:760px;margin:0 auto;padding:28px 16px 60px}
.card{background:rgba(255,255,255,.88);border:2px solid #ffe0eb;border-radius:30px;padding:clamp(22px,5vw,42px);
box-shadow:0 18px 55px #c85b7a20;text-align:center}
.eyebrow{letter-spacing:2px;text-transform:uppercase;font-size:.75rem;color:var(--deep);font-weight:800}
h1{font-size:clamp(2rem,7vw,3.4rem);line-height:1.08;margin:12px 0;color:#a93d69}
p{line-height:1.65}
.elephant{font-size:5rem;display:block;filter:drop-shadow(0 5px 0 #ffd7e5);margin:4px}
.tiny{font-size:.95rem;color:#93677a}
button,.btn{border:0;border-radius:999px;padding:14px 24px;font-weight:800;font-size:1rem;cursor:pointer;transition:transform .15s,box-shadow .15s}
button:hover,.btn:hover{transform:translateY(-2px)}
.yes{background:linear-gradient(135deg,#ff7da8,#f05b92);color:white;box-shadow:0 8px 18px #f05b9240}
.no{background:#f4edf0;color:#946e7e;position:relative}
.actions{display:flex;justify-content:center;gap:14px;align-items:center;flex-wrap:wrap;margin:25px 0 8px;min-height:60px}
.hidden{display:none!important}
.progress{display:flex;justify-content:center;gap:7px;margin-bottom:22px}
.dot{height:8px;width:36px;border-radius:99px;background:#f5d5e0}.dot.active{background:#f36b9b}
.section-title{font-size:1.55rem;color:#a93d69;margin:8px 0}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(190px,1fr));gap:12px;margin:22px 0;text-align:left}
.option{display:block;border:2px solid #f6dce5;background:#fffafb;padding:14px;border-radius:17px;cursor:pointer;transition:.15s}
.option:has(input:checked){border-color:#f36b9b;background:#fff0f5;box-shadow:0 5px 15px #f36b9b18}
.option input{accent-color:#e8548a;margin-right:8px}
.option strong{display:block;margin-bottom:4px}
.option small{color:#987184}
.field{text-align:left;margin:18px 0}
label.fieldlabel{display:block;font-weight:800;margin-bottom:8px}
input[type=date],input[type=text],select{width:100%;padding:13px;border:2px solid #f3d9e3;border-radius:14px;background:white;color:var(--ink);font:inherit}
.footer{margin-top:18px;font-size:.82rem;color:#a17b8b}
.summary{background:#fff2f7;border-radius:18px;padding:18px;text-align:left;margin:18px 0;white-space:pre-line}
@media(max-width:480px){.card{border-radius:24px}.grid{grid-template-columns:1fr}.elephant{font-size:4.3rem}}
</style>
</head>
<body>
<div id="floating"></div>
<main>
  <div class="progress" id="progress"><span class="dot active"></span><span class="dot"></span><span class="dot"></span></div>
  <section class="card" id="step1">
    <div class="eyebrow">a tiny question 💌</div>
    <span class="elephant" aria-label="cute elephant">🐘💗</span>
    <h1>Will you go on a date with me?</h1>
    <p>I was thinking… you, me, something yummy, and a little memory to keep. 🥹</p>
    <div class="actions">
      <button class="yes" onclick="goTo(2)">YES! 💖</button>
      <button class="no" id="noBtn" aria-label="No, playfully dodging">No 🙈</button>
    </div>
    <p class="tiny" id="tease">Psst… the elephant is rooting for YES. 🐘</p>
    <div class="footer">made with a little courage and lots of 💗</div>
  </section>

  <section class="card hidden" id="step2">
    <div class="eyebrow">chapter 2 · the plan</div>
    <span class="elephant">🐘💕</span>
    <h2 class="section-title">Yay! Let's plan our little date ✨</h2>
    <p>Pick a café that sounds lovely. These are popular Pune picks; we can check opening hours before going.</p>
    <div class="grid" id="cafes">
      <label class="option"><input type="radio" name="cafe" value="German Bakery — Koregaon Park" required><strong>🥐 German Bakery</strong><small>Koregaon Park · bakery & café</small></label>
      <label class="option"><input type="radio" name="cafe" value="Cafe Goodluck — Deccan"><strong>☕ Café Goodluck</strong><small>Deccan · iconic Pune favourite</small></label>
      <label class="option"><input type="radio" name="cafe" value="Waari Book Cafe — Kothrud"><strong>📚 Waari Book Café</strong><small>Kothrud · books and coffee</small></label>
      <label class="option"><input type="radio" name="cafe" value="Cafe Kathaa — FC Road"><strong>🌷 Café Kathaa</strong><small>FC Road · cosy café vibe</small></label>
      <label class="option"><input type="radio" name="cafe" value="The French Window Patisserie — Koregaon Park"><strong>🍰 The French Window</strong><small>Koregaon Park · pastries & desserts</small></label>
      <label class="option"><input type="radio" name="cafe" value="Cafe From The Tree — Koregaon Park"><strong>🌿 Café From The Tree</strong><small>Koregaon Park · relaxed café</small></label>
      <label class="option"><input type="radio" name="cafe" value="Cafe Flying Gypsy's — Shivajinagar"><strong>🪴 Café Flying Gypsy's</strong><small>Shivajinagar · coffee & chill</small></label>
    </div>
    <div class="field"><label class="fieldlabel" for="date">What date works for you? (optional) 📅</label><input type="date" id="date"></div>
    <div class="actions"><button class="no" onclick="goTo(1)">← Back</button><button class="yes" onclick="goTo(3)">Next, food please! 🍓</button></div>
  </section>

  <section class="card hidden" id="step3">
    <div class="eyebrow">chapter 3 · food is important</div>
    <span class="elephant">🐘🍓</span>
    <h2 class="section-title">What are you craving? 😋</h2>
    <p>Choose as many as you like. There are no wrong answers (except stealing the last bite… maybe). 💕</p>
    <div class="grid" id="foods">
      <label class="option"><input type="checkbox" value="Pizza"><strong>🍕 Pizza</strong><small>cheesy happiness</small></label>
      <label class="option"><input type="checkbox" value="Pasta / Italian"><strong>🍝 Pasta / Italian</strong><small>comfort food</small></label>
      <label class="option"><input type="checkbox" value="Burgers & fries"><strong>🍔 Burgers & fries</strong><small>classic combo</small></label>
      <label class="option"><input type="checkbox" value="Momos"><strong>🥟 Momos</strong><small>steamed or crispy</small></label>
      <label class="option"><input type="checkbox" value="Chinese / Asian"><strong>🥡 Chinese / Asian</strong><small>noodles, rice, more</small></label>
      <label class="option"><input type="checkbox" value="Indian / North Indian"><strong>🧈 Indian / North Indian</strong><small>naan, paneer, etc.</small></label>
      <label class="option"><input type="checkbox" value="Maharashtrian"><strong>🥘 Maharashtrian</strong><small>local favourites</small></label>
      <label class="option"><input type="checkbox" value="South Indian"><strong>🥞 South Indian</strong><small>dosa, idli, uttapam</small></label>
      <label class="option"><input type="checkbox" value="Mexican"><strong>🌮 Mexican</strong><small>tacos and nachos</small></label>
      <label class="option"><input type="checkbox" value="Sandwiches / wraps"><strong>🥪 Sandwiches / wraps</strong><small>light and tasty</small></label>
      <label class="option"><input type="checkbox" value="Desserts / waffles / pancakes"><strong>🧇 Desserts / waffles</strong><small>sweet tooth time</small></label>
      <label class="option"><input type="checkbox" value="Ice cream"><strong>🍦 Ice cream</strong><small>always a good idea</small></label>
      <label class="option"><input type="checkbox" value="Cakes / pastries"><strong>🍰 Cakes / pastries</strong><small>a little treat</small></label>
      <label class="option"><input type="checkbox" value="Coffee / tea / matcha"><strong>🧋 Coffee / tea / matcha</strong><small>sip and chat</small></label>
      <label class="option"><input type="checkbox" value="Street food / chaat"><strong>🥙 Street food / chaat</strong><small>pani puri, chaat, etc.</small></label>
      <label class="option"><input type="checkbox" value="Anything vegetarian"><strong>🥗 Vegetarian</strong><small>veg-friendly picks</small></label>
    </div>
    <div class="field"><label class="fieldlabel" for="notes">Any food allergies or little requests? (optional)</label><input type="text" id="notes" placeholder="Tell me here…"></div>
    <div class="actions"><button class="no" onclick="goTo(2)">← Back</button><button class="yes" onclick="makePlan()">Make our date plan 💌</button></div>
  </section>

  <section class="card hidden" id="step4">
    <div class="eyebrow">officially a cute plan</div>
    <span class="elephant">🐘💞</span>
    <h1>Our little date plan!</h1>
    <p>Okay, this is already making me smile. 🥹</p>
    <div class="summary" id="summary"></div>
    <p>Now send the plan back so we can make it happen. 💗</p>
    <div class="actions">
      <button class="yes" onclick="shareWhatsApp()">Send on WhatsApp 💚</button>
      <button class="yes" onclick="shareEmail()">Send by email 💌</button>
      <button class="no" onclick="copyPlan()">Copy plan 📋</button>
    </div>
    <p class="tiny" id="copyStatus"></p>
    <button class="no" onclick="goTo(2)">Change choices</button>
    <div class="footer">No pressure, just a sweet invitation. 💗</div>
  </section>
</main>
<script>
const noBtn=document.getElementById('noBtn');
let dodges=0;
function dodge(){
  dodges++;
  const messages=['Hehe, too slow 🙈','The elephant says… maybe YES? 🐘','Oopsie! 💨','That button has places to be 💗','One more try? 😳'];
  document.getElementById('tease').textContent=messages[(dodges-1)%messages.length];
  // Move within the viewport so it stays playful on both desktop and mobile.
  const maxX=Math.max(8,window.innerWidth-noBtn.offsetWidth-16);
  const maxY=Math.max(8,window.innerHeight-noBtn.offsetHeight-16);
  noBtn.style.position='fixed';
  noBtn.style.left=(8+Math.random()*Math.max(1,maxX-8))+'px';
  noBtn.style.top=(8+Math.random()*Math.max(1,maxY-8))+'px';
  noBtn.style.zIndex='10';
}
noBtn.addEventListener('mouseenter',dodge);
noBtn.addEventListener('pointerdown',e=>{e.preventDefault();dodge();});
noBtn.addEventListener('focus',dodge);
function goTo(n){
  [1,2,3,4].forEach(i=>document.getElementById('step'+i).classList.toggle('hidden',i!==n));
  document.querySelectorAll('.dot').forEach((d,i)=>d.classList.toggle('active',i===Math.min(n-1,2)));
  window.scrollTo({top:0,behavior:'smooth'});
  if(n===1){noBtn.style.position='relative';noBtn.style.left='';noBtn.style.top='';}
}
function selectedCafe(){return document.querySelector('input[name="cafe"]:checked')?.value||'';}
function selectedFoods(){return [...document.querySelectorAll('#foods input:checked')].map(x=>x.value);}

function planText(){
  const cafe = selectedCafe() || 'To be decided together';
  const date = document.getElementById('date').value || 'Whenever works for us';
  const foods = selectedFoods();
  const notes = document.getElementById('notes').value.trim();

  return '💗 OUR LITTLE DATE PLAN 💗\n\n' +
    '📍 Café: ' + cafe + '\n' +
    '📅 Date: ' + date + '\n' +
    '🍓 Food cravings: ' +
    (foods.length ? foods.join(', ') : 'Surprise me!') +
    (notes ? '\n📝 Notes: ' + notes : '') +
    '\n\n🐘 Made with a little courage and lots of love.';
}
function makePlan(){
  if(!selectedCafe()){alert('Pick a café first, cutie 💗');return;}
  document.getElementById('summary').textContent=planText();
  goTo(4);
}
function shareWhatsApp(){window.open('https://wa.me/?text='+encodeURIComponent(planText()),'_blank');}
function shareEmail(){window.location.href='mailto:?subject='+encodeURIComponent('Our little date plan 💗')+'&body='+encodeURIComponent(planText());}
async function copyPlan(){
  try{await navigator.clipboard.writeText(planText());document.getElementById('copyStatus').textContent='Copied! Paste it into your chat 💗';}
  catch(e){document.getElementById('copyStatus').textContent='Select and copy the plan above to share it 💗';}
}
const floatBox=document.getElementById('floating');
for(let i=0;i<15;i++){const s=document.createElement('span');s.className='heart';s.textContent=['💗','♡','💕','♥'][i%4];s.style.left=(Math.random()*100)+'%';s.style.animationDelay=(Math.random()*9)+'s';s.style.animationDuration=(7+Math.random()*7)+'s';s.style.fontSize=(14+Math.random()*20)+'px';floatBox.appendChild(s);}
</script>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(PAGE)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port= int(__import__("os").environ.get("PORT", 5000)), debug=False)
