# Import the necessary libraries for the emotion detector app
import requests

def emotion_detector(text_to_analyse):
    '''Detect the emotion in a given English text using a remote NLP API'''
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    # Send POST request
    response = requests.post(url, json=myobj, headers=header, timeout=10)
    # Handle blank input via status_code == 400
    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    # Normal path (200)
    data = response.json()
    preds = data['emotionPredictions']
    emotions = preds[0]['emotion']
    # Determine dominant emotion (name only)
    dominant_emotion = max(emotions, key=emotions.get)
    # Return flat dictionary format
    return {
        'anger': emotions['anger'], 
        'disgust': emotions['disgust'], 
        'fear': emotions['fear'],
        'joy': emotions['joy'],
        'sadness': emotions['sadness'],
        'dominant_emotion': dominant_emotion
    }