''' Flask-app which detects emotions via /emotionDetector and serves the indexpage.'''
# Import Flask, render_template, request from the flask framework package.
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector
# Initiate the Flask app
app = Flask("EmotionDetector")
@app.route("/emotionDetector")
def sent_detector():
    """Executes emotion detection on the queryparam 'textToAnalyze' 
    and gives back emotion scores as a string."""
    text_to_analyze = request.args.get('textToAnalyze')
    # Call detector -> expects flat dict per Task 3
    r = emotion_detector(text_to_analyze)
    # Show message if detector reports no dominant emotion (e.g., blank input)
    if r.get('dominant_emotion') is None:
        return "Invalid text! Please try again!"
    # Format exact according to requirement
    result_text = (
        f"For the given statement, the system response is "
        f"'anger': {r['anger']}, "
        f"'disgust': {r['disgust']}, "
        f"'fear': {r['fear']}, "
        f"'joy': {r['joy']} and "
        f"'sadness': {r['sadness']}. "
        f"'dominant emotion': {r['dominant_emotion']}."
    )
    return result_text
@app.route("/")
def render_index_page():
    ''' This function renders the startpage of the detector app '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
