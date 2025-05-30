''' Executing this function initiates the application of emotion detection 
    to be executed over the Flask channel and deployed on localhost:5000.
'''
# Import Flask, render_template, request from the flask pramework package
from flask import Flask, request, render_template
# Import the emotion_detector function from the package created
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_detector():
    ''' This function runs emotion_detector on the text entered by the user
    '''
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)

    # For the given statement, the system response is 'anger': 0.006274985, 
    # 'disgust': 0.0025598293, 'fear': 0.009251528, 'joy': 0.9680386 and 'sadness': 0.049744144. 
    # The dominant emotion is joy. 

    # Pop the dominant emotion so we can use special formatting on it later.
    dominant_value = response.pop("dominant_emotion", None)
    if dominant_value is not None:
        response_text = "For the given statement, the system response is "
        for key, value in response.items():
            response_text = response_text + f"'{key}': {value},"

        # Replace the last comma with a period.
        response_text[-1] = '.'
        # Add the dominant emotion.
        response_text = response_text + f" The dominant emotion is <b>{dominant_value}</b>."
        return response_text

    return f"Invalid input: {text_to_analyze}! Try again."

if __name__ == "__main__":
    ''' This functions executes the flask app and deploys it on localhost:5000
    '''
    app.run(host="0.0.0.0", port=5000)
