from flask import Flask, request, jsonify, render_template_string
from ai_server import inviteMessage

app = Flask(__name__)

HTML = """
<!doctype html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Chat</title>
  <style>
    :root {
      --bg: #0d0d0d;
      --surface: #161616;
      --surface-alt: #1f1f1f;
      --border: #2a2a2a;
      --text: #e5e5e5;
      --text-dim: #737373;
      --accent: #fff;
      --radius: 8px;
    }
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      font-family: 'SF Mono', 'Fira Code', monospace;
      background: var(--bg);
      color: var(--text);
      min-height: 100vh;
      display: flex;
      justify-content: center;
      padding: 40px 20px;
    }
    .chat {
      width: 100%;
      max-width: 520px;
      display: flex;
      flex-direction: column;
      gap: 24px;
    }
    .chat-header {
      padding-bottom: 16px;
      border-bottom: 1px solid var(--border);
    }
    .chat-header h1 {
      font-size: 14px;
      font-weight: 500;
      letter-spacing: 0.5px;
      text-transform: uppercase;
      color: var(--text-dim);
    }
    .messages {
      flex: 1;
      display: flex;
      flex-direction: column;
      gap: 20px;
      min-height: 300px;
    }
    .msg {
      max-width: 85%;
      padding: 12px 16px;
      font-size: 13px;
      line-height: 1.6;
    }
    .msg.you {
      align-self: flex-end;
      background: var(--surface-alt);
      border-radius: var(--radius) var(--radius) 2px var(--radius);
    }
    .msg.ai {
      align-self: flex-start;
      background: transparent;
      border: 1px solid var(--border);
      border-radius: var(--radius) var(--radius) var(--radius) 2px;
      color: var(--text-dim);
    }
    .input-row {
      display: flex;
      gap: 12px;
      padding-top: 16px;
      border-top: 1px solid var(--border);
    }
    .input-row input {
      flex: 1;
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 14px 16px;
      color: var(--text);
      font-family: inherit;
      font-size: 13px;
      outline: none;
      transition: border-color 0.2s;
    }
    .input-row input::placeholder { color: var(--text-dim); }
    .input-row input:focus { border-color: var(--text-dim); }
    .input-row button {
      background: var(--text);
      color: var(--bg);
      border: none;
      border-radius: var(--radius);
      padding: 14px 24px;
      font-family: inherit;
      font-size: 12px;
      font-weight: 600;
      text-transform: uppercase;
      letter-spacing: 1px;
      cursor: pointer;
      transition: opacity 0.2s;
    }
    .input-row button:hover { opacity: 0.8; }
  </style>
</head>
<body>
  <div class="chat">
    <div class="chat-header">
      <h1>Terminal</h1>
    </div>
    <div class="messages" id="msgs"></div>
    <div class="input-row">
      <input id="txt" placeholder="digite..." onkeydown="if(event.key==='Enter')send()">
      <button onclick="send()">Enviar</button>
    </div>
  </div>
<script>
const msgs=document.getElementById('msgs');
const txt=document.getElementById('txt');
async function send(){
  const v=txt.value.trim();
  if(!v)return;
  msgs.innerHTML+=`<div class="msg you">${v}</div>`;
  msgs.innerHTML+=`<div class="msg ai">...</div>`;
  msgs.scrollTop=msgs.scrollHeight;
  txt.value='';
  try{
    const r=await fetch('/chat',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({message:v})});
    const d=await r.json();
    document.querySelectorAll('.msg.ai').item(document.querySelectorAll('.msg.ai').length-1).textContent=d.reply;
  }catch(e){
    document.querySelectorAll('.msg.ai').item(document.querySelectorAll('.msg.ai').length-1).textContent='erro';
  }
  msgs.scrollTop=msgs.scrollHeight;
}
</script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML)

@app.route('/chat', methods=['POST'])
def chat():
    payload = request.get_json()
    user_msg = payload.get('message', '')
    reply = inviteMessage(user_msg)
    return jsonify({'reply': reply})

@app.route('/ping')
def ping():
    return 'OK'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
