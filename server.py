''' 
Executing this function initiates the application of emotion
detection to be executed over the Flask channel and deployed on
localhost:5000.
'''

# Importar Flask, render_template y request
from flask import Flask, render_template, request

# Importar la función emotion_detector del paquete creado
from EmotionDetection.emotion_detection import emotion_detector

# Inicializar la aplicación Flask
app = Flask("Emotion Detector")


@app.route("/emotionDetector")
def emo_detector():
    '''
    Función para analizar emociones
    '''

    # Recuperar el texto a analizar desde la solicitud
    text_to_analyze = request.args.get('textToAnalyze')

    # Pasar el texto a la función emotion_detector
    response = emotion_detector(text_to_analyze)

    # Extraer resultados
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    # Validar entrada inválida
    if dominant_emotion is None:
        return "Invalid text! Please try again."

    # Retornar respuesta formateada
    return f"For the given statement, the system response is " \
           f"'anger': {anger}, " \
           f"'disgust': {disgust}, " \
           f"'fear': {fear}, " \
           f"'joy': {joy} and " \
           f"'sadness': {sadness}. " \
           f"The dominant emotion is {dominant_emotion}."


@app.route("/")
def render_index_page():
    '''
    Renderiza la página principal
    '''
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)