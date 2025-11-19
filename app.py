from flask import Flask, request, jsonify, render_template
import requests
import os

app = Flask(__name__)

# URL de llama-swap (OpenAI-compatible API)
LLM_URL = os.getenv('LLM_URL', 'http://llama-swap:8090')
LLM_MODEL = os.getenv('LLM_MODEL', 'qwen2.5-coder:32b')

@app.route('/')
def home():
    return render_template('chat.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        pregunta = data.get('prompt', '').strip()

        if not pregunta:
            return jsonify({'error': 'Escribe un mensaje'}), 400

        # Llamar a llama-swap usando API compatible con OpenAI
        respuesta = requests.post(f'{LLM_URL}/v1/chat/completions', json={
            'model': LLM_MODEL,
            'messages': [
                {'role': 'system', 'content': 'Eres un asistente útil. Responde siempre en español.'},
                {'role': 'user', 'content': pregunta}
            ],
            'temperature': 0.7,
            'max_tokens': 500
        }, timeout=60)

        if respuesta.status_code == 200:
            resultado = respuesta.json()
            return jsonify({
                'response': resultado['choices'][0]['message']['content'],
                'success': True
            })
        else:
            return jsonify({
                'error': f'LLM error: {respuesta.status_code}',
                'success': False
            })

    except Exception as e:
        return jsonify({
            'error': f'Error: {str(e)}',
            'success': False
        }), 500

if __name__ == '__main__':
    print("🤖 ChatBot con llama.cpp + llama-swap iniciado")
    print(f"📡 LLM: {LLM_URL}")
    print(f"🧠 Modelo: {LLM_MODEL}")
    print("🌐 Web: http://localhost:5000")
    app.run(host='0.0.0.0', port=5000, debug=False)