from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('chat.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    pregunta = request.json.get('prompt', '').strip()
    
    # Respuesta básica por ahora
    if 'hola' in pregunta.lower():
        respuesta = "¡Hola! Soy tu chatbot ¿En qué puedo ayudarte?"
    elif 'nombre' in pregunta.lower():
        respuesta = "Soy ChatBot para testear Docker"
    else:
        respuesta = f"Recibí tu mensaje: '{pregunta}'. Pronto tendré más inteligencia con Ollama!"
    
    return jsonify({'response': respuesta})

if __name__ == '__main__':
    print("ChatBot iniciado en http://localhost:5000")
    app.run(host='0.0.0.0', port=5000, debug=False)