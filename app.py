from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story, excited_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

# @app.get("/")
# def home_page():


#     return render_template('home.html')



@app.get('/questions')
def display_form(): #TODO: make function names more specific
    """ makes form with input fields matching the story prompts"""
    story = request.args.get("story-options")
    prompts = story.prompts

    return render_template('questions.html', prompts=prompts)


@app.get("/results")
def display_results():
    """ gets form data from user, displays new story with user input """

    story = silly_story.get_result_text(request.args)
    return render_template("results.html", story=story)
