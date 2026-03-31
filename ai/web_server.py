from flask import Flask, request, jsonify, render_template_string
from ai_server import inviteMessage

app = Flask(__name__)

HTML = """
<!doctype html>
<html><body>
<h2>TESTE AI</h2>
<div id="log" style="white-space: pre-line; margin-bottom:1em;"></div>
<input id="msg" placeholder="Sua mensagem" style="width:80%">
<button onclick="send()">Enviar</button>
<script>
async function send(){
  const txt=document.getElementById('msg').value;
  const res=await fetch('/chat', {method:'POST',
        headers:{'Content-Type':'application/json'},
        body:JSON.stringify({message:txt})});
  const data=await res.json();
  document.getElementById('log').textContent += 'Você: '+txt+'\\nAI: '+data.reply+'\\n\\n';
  document.getElementById('msg').value='';
}
</script>
</body></html>
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
    app.run(host='0.0.0.0', port=5000, debug=True)