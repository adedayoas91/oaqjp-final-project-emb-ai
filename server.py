from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion detector")

@app.route("/emotionDetector")
def sent_analyzer():
    text_to_analyze = request.args.get('textToAnalyze')

    emotion = emotion_detector(text_to_analyze)
    dominant_emotion = max(emotion, key=emotion.get)
    statement = f"""For the given statement, the system response is 'anger': {emotion['anger']},
            'disgust': {emotion['disgust']}, 'fear': {emotion['fear']}, 'joy': {emotion['joy']} 
            and 'sadness': {emotion['sadness']}. The dominant emotion is {dominant_emotion}."""    
    return statement

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
