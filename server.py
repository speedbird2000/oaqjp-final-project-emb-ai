''' Executing this function initiates the application of 
    emotion detection to be executed over the Flask channel and deployed on
    localhost:5000.
'''
# Import Flask, render_template, request from the flask pramework package.
# Import the emotion_detector function from the package created.
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app.
app = Flask("EmotionDetector")

@app.route("/emotionDetector")
def sent_detector():
    """Executes emotion detection on the queryparam 'textToAnalyze' 
    and gives back emotion scores as a string."""
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    return f"For the given statement, the system response is {str(response['emotions'])[1:-1]}"
@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    # executes the flask app and deploys it on localhost:5000
    app.run(host="0.0.0.0", port=5000)
