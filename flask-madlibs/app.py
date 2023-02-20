from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)
app.config['SECRET_KEY'] = "s"
@app.route("/")
def q():
    p = story.prompts
    return render_template("questions.html", prompts=p)

@app.route("/story")
def show_story():
    text = story.generate(request.args)

    return render_template("story.html", text=text)