from flask import Flask, render_template, request
import random, os
from batch_screenshots import take_screenshots
from make_collage import create_collage

app = Flask(__name__)

# --- MadLibs Templates ---
from templates_list import madlib_templates

# ------------------ ROUTES ------------------

@app.route("/")
def home():
    return render_template("home.html")

# --- MadLibs ---
@app.route("/madlibs", methods=["GET", "POST"])
def madlibs():
    story = None
    if request.method == "POST":
        noun = request.form.get("noun")
        verb = request.form.get("verb")
        adjective = request.form.get("adjective")
        place = request.form.get("place")

        if not (noun and verb and adjective and place):
            story = "⚠️ Please fill all fields!"
        else:
            story_template = random.choice(madlib_templates)
            story = story_template.format(
                noun=noun, verb=verb, adjective=adjective, place=place
            )

    return render_template("index.html", story=story)

# --- Batch Screenshots ---
@app.route("/screenshots", methods=["GET", "POST"])
def screenshots():
    images = None
    if request.method == "POST":
        folder = "static/screenshots"
        take_screenshots(folder, count=5)
        files = os.listdir(folder)
        images = [f"screenshots/{f}" for f in files if f.endswith(".png")]
    return render_template("screenshots.html", images=images)

# --- Make Collage ---
@app.route("/collage", methods=["GET", "POST"])
def collage():
    collage_path = None
    if request.method == "POST":
        output_file = "static/collage_output.jpg"
        create_collage("static/screenshots", output_file)
        collage_path = "collage_output.jpg"
    return render_template("collage.html", collage_path=collage_path)

if __name__ == "__main__":
    app.run(debug=True)
