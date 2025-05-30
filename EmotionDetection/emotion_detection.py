''' This module performs emotion detection.
'''
import json
import requests

def emotion_detector(text_to_analyse):
    ''' This function performs emotion detection on given text.
    '''
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = {"raw_document": {"text": text_to_analyse }}
    response = requests.post(url, json = myobj, headers=header)

    # Error Handling for invalid input
    # Code in server.py will check for dominant_emotion equal to None
    # and display an appropriate error message.
    if response.status_code == 400:
        return {'dominant_emotion': None}

    formatted_response = json.loads(response.text)
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    max_key = max(emotions, key=emotions.get)
    emotions['dominant_emotion'] = max_key

    return emotions
