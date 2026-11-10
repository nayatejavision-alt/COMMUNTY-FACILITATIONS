from flask import Flask, render_template, request, redirect
import os

app = Flask(__name__)

# ఇక్కడ మనం సింపుల్ గా హోమ్ పేజ్ మరియు డేటా సబ్మిట్ చేసే లాజిక్ రాస్తాం
@app.route('/')
def home():
    return "Welcome to Community Facilitation Project!"

if __name__ == '__main__':
    app.run(debug=True)
