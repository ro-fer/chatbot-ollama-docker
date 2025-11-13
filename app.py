from flask import Flask, request, jsonify, render_template
import requests
import os

app = Flask(__name__)

# URL de Ollama (local en desarrollo, remoto en producción)
OLLAMA_URL = os.getenv('OLLAMA_URL', 'http://ollama:11434')

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
        
        # Llamar a Ollama
        respuesta = requests.post(f'{OLLAMA_URL}/api/generate', json={
            'model': 'llama2',
            'prompt': f"Responde en español de manera útil: {pregunta}",
            'stream': False
        }, timeout=30)
        
        if respuesta.status_code == 200:
            return jsonify({
                'response': respuesta.json()['response'],
                'success': True
            })
        else:
            return jsonify({
                'error': f'Ollama error: {respuesta.status_code}',
                'success': False
            })
            
    except Exception as e:
        return jsonify({
            'error': f'Error: {str(e)}',
            'success': False
        }), 500

if __name__ == '__main__':
    print(" ChatBot con Ollama iniciado")
    print(f" Ollama: {OLLAMA_URL}")
    print("Web: http://localhost:5000")
    app.run(host='0.0.0.0', port=5000, debug=False)