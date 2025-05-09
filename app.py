from flask import Flask, render_template, request
from nrclex import NRCLex

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    emotions = {}
    top_emotions = []
    if request.method == 'POST':
        text = request.form['text']
        if text.strip():
            emotion = NRCLex(text)
            emotions = emotion.raw_emotion_scores
            top_emotions = emotion.top_emotions
    return render_template('index.html', emotions=emotions, top_emotions=top_emotions)

if __name__ == '__main__':
    app.run(debug=True) 
