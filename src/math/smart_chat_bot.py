import os
import webbrowser
import json
from http.server import HTTPServer, BaseHTTPRequestHandler
import threading
from openai import OpenAI
import time

# ====== НАСТРОЙКИ ======
API_KEY = "sk-or-v1....."  # ТВОЙ КЛЮЧ
MODEL = "deepseek/deepseek-r1:free"  # БЕСПЛАТНАЯ МОДЕЛЬ DEEPSEEK

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=API_KEY,
)

# ====== HTTP-СЕРВЕР ======
class ChatHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path == "/chat":
            try:
                length = int(self.headers.get("Content-Length", 0))
                body = self.rfile.read(length)
                data = json.loads(body)
                user_message = data.get("message", "")

                completion = client.chat.completions.create(
                    model=MODEL,
                    messages=[
                        {"role": "system", "content": "Ты — полезный ассистент по математике. Отвечай кратко и понятно."},
                        {"role": "user", "content": user_message}
                    ],
                    temperature=0.7,
                )
                reply = completion.choices[0].message.content
            except Exception as e:
                reply = f"❌ Ошибка: {str(e)}"

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"reply": reply}).encode())
        else:
            self.send_response(404)
            self.end_headers()

    def log_message(self, format, *args):
        pass

# ====== ЗАПУСК СЕРВЕРА ======
server = None

def start_server():
    global server
    server = HTTPServer(("127.0.0.1", 5000), ChatHandler)
    print("🧠 Сервер ИИ запущен на http://127.0.0.1:5000")
    server.serve_forever()

# ====== ОТКРЫТИЕ ЧАТА ======
def open_smart_chat():
    print("🔍 open_smart_chat вызвана!")
    
    html_content = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Умный чат-бот</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Segoe UI', sans-serif;
            background: #0b1120;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        .chat-container {
            width: 500px;
            max-width: 95%;
            background: #1e293b;
            border-radius: 20px;
            padding: 25px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.8);
            border: 1px solid #334155;
        }
        h2 {
            color: #94a3b8;
            text-align: center;
            margin-bottom: 15px;
        }
        .chat-box {
            background: #0f172a;
            border-radius: 12px;
            padding: 15px;
            height: 320px;
            overflow-y: auto;
            margin-bottom: 15px;
            border: 1px solid #334155;
        }
        .chat-box p {
            color: #e2e8f0;
            font-size: 14px;
            padding: 8px 12px;
            border-radius: 10px;
            margin: 6px 0;
            line-height: 1.5;
        }
        .user-msg {
            background: #2563eb;
            text-align: right;
            border-bottom-right-radius: 0;
        }
        .bot-msg {
            background: #1e293b;
            text-align: left;
            border-bottom-left-radius: 0;
            border-left: 3px solid #3b82f6;
        }
        .input-area {
            display: flex;
            gap: 10px;
        }
        .input-area input {
            flex: 1;
            padding: 12px 15px;
            border-radius: 30px;
            border: none;
            background: #0f172a;
            color: #f1f5f9;
            font-size: 14px;
            outline: none;
            border: 1px solid #334155;
        }
        .input-area input::placeholder {
            color: #64748b;
        }
        .input-area button {
            padding: 12px 22px;
            border: none;
            border-radius: 30px;
            background: #3b82f6;
            color: white;
            font-weight: bold;
            cursor: pointer;
            transition: 0.3s;
        }
        .input-area button:hover {
            background: #2563eb;
            transform: scale(1.02);
        }
        .footer-chat {
            text-align: center;
            margin-top: 12px;
            color: #475569;
            font-size: 12px;
        }
    </style>
</head>
<body>
<div class="chat-container">
    <h2>🧠 Умный чат-бот (DeepSeek)</h2>
    <div class="chat-box" id="chatBox">
        <p class="bot-msg">Привет! Я работаю на DeepSeek. Задай любой вопрос по математике.</p>
    </div>
    <div class="input-area">
        <input type="text" id="userInput" placeholder="Напиши вопрос...">
        <button onclick="sendMessage()">Отправить</button>
    </div>
    <div class="footer-chat">Блок 3. Основы математики и информатики</div>
</div>

<script>
    const chatBox = document.getElementById('chatBox');
    const input = document.getElementById('userInput');

    function addMessage(text, type) {
        const p = document.createElement('p');
        p.className = type === 'user' ? 'user-msg' : 'bot-msg';
        p.textContent = text;
        chatBox.appendChild(p);
        chatBox.scrollTop = chatBox.scrollHeight;
    }

    function sendMessage() {
        const msg = input.value.trim();
        if (!msg) return;
        addMessage(msg, 'user');
        input.value = '';
        addMessage('⏳ Думаю...', 'bot');

        fetch('http://127.0.0.1:5000/chat', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ message: msg })
        })
        .then(res => res.json())
        .then(data => {
            const msgs = chatBox.querySelectorAll('.bot-msg');
            msgs[msgs.length - 1].textContent = data.reply;
        })
        .catch(() => {
            const msgs = chatBox.querySelectorAll('.bot-msg');
            msgs[msgs.length - 1].textContent = '❌ Ошибка соединения. Запусти сервер.';
        });
    }

    input.addEventListener('keydown', function(e) {
        if (e.key === 'Enter') sendMessage();
    });
</script>
</body>
</html>
    """

    with open("data/smart_chat.html", "w", encoding="utf-8") as f:
        f.write(html_content)

    # Запускаем сервер в фоне
    thread = threading.Thread(target=start_server, daemon=True)
    thread.start()
    
    # Даём серверу время запуститься
    time.sleep(2)

    # Открываем браузер
    full_path = os.path.abspath("data/smart_chat.html")
    webbrowser.open(full_path)
    print(f"✅ УМНЫЙ ЧАТ-БОТ ОТКРЫТ: {full_path}")

if __name__ == "__main__":
    print("🔍 Запуск через __main__")
    open_smart_chat()