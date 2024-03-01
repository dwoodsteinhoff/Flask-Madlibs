from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)

app.config['SECRET_KEY'] = "chickenzarecool21837"

debug = DebugToolbarExtension(app)

@app.route('/')
def home_page():
    prompts = story.prompts
    return render_template('home_page.html', prompts = prompts)

@app.route('/story')
def make_story():
    the_story = story.generate(request.args)
    return render_template('story.html', story = the_story)