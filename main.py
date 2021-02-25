from flask import Flask, render_template

app = Flask("maKlausCovid")

@app.route("/")
def index():
    return render_template("index.html")

app.run()