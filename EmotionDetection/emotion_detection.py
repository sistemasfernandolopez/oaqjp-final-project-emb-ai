import requests # Importar la biblioteca requests para manejar solicitudes HTTP
import json

def emotion_detector(text_to_analyse):     # Definir una función llamada emotion_detector que toma una entrada de tipo cadena (text_to_analyse) 
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'     # URL del servicio de prediccion de emociones
    myobj = { "raw_document": { "text": text_to_analyse } }     # Crear un diccionario con el texto a analizar 
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}     # Establecer las cabeceras requeridas para la solicitud API 
    response = requests.post(url, json = myobj, headers=header)     # Enviar una solicitud POST a la API con el texto y las cabeceras 
    
    # Manejo de error para entrada vacía
    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    # Convertir la respuesta JSON en diccionario
    formatted_response = json.loads(response.text)

    # Extraer las emociones
    emotions = formatted_response["emotionPredictions"][0]["emotion"]

    anger_score = emotions["anger"]
    disgust_score = emotions["disgust"]
    fear_score = emotions["fear"]
    joy_score = emotions["joy"]
    sadness_score = emotions["sadness"]

    # Crear diccionario de emociones
    emotion_scores = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score
    }

    # Encontrar la emoción dominante
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)

    # Agregar emoción dominante al resultado
    emotion_scores['dominant_emotion'] = dominant_emotion

    return emotion_scores