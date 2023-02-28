from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def index(name=None):
    return render_template('index.html', name=name)

@app.route("/select")
def select(name=None):
    return render_template('select.html', name=name)


@app.route("/about")
def about(name=None):
    return render_template('about.html', name=name)

@app.route("/help")
def help(name=None):
    return render_template('help.html', name=name)

@app.route("/map")
def map(name=None):
    return render_template('map.html', name=name)




