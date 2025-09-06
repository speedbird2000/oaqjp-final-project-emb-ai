''' Import the nescessary libraries for the emotion detector app '''
import requests , json

def emotion_detector(text_to_analyse):
    ''' this function is to detect the emotinon in a given text '''    
    # URL of the emotion detection service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    # Constructing the request payload in the expected format
    myobj = { "raw_document": { "text": text_to_analyse } }
    # Custom header specifying the model ID for the emotion detector service
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    # Sending a POST request to the sentiment analysis API
    response = requests.post(url, json=myobj, headers=header)
    # Parsing the JSON response from the API 
    data = response.json() 
    # get the list 
    preds = data.get('emotionPredictions') 
    # first item from the list 
    emotions = preds[0].get('emotion', {}) 
    # following are the 'emotion' items
    anger = emotions.get('anger')
    disgust = emotions.get('disgust') 
    fear = emotions.get('fear') 
    joy = emotions.get('joy') 
    sadness = emotions.get('sadness') 
    # determine dominant emotion
    best_label = None
    best_score = -1.0
    # fixed order along the known keys
    for key in ['joy', 'anger', 'disgust', 'fear', 'sadness']:
        value = emotions.get(key)
        if isinstance(value, (int, float)) and value > best_score:
            best_label = key
            best_score = value
    # return dominant emotion and the other emotions
    return {'dominant': {'label': best_label, 'score': best_score}, 'emotions': emotions}

