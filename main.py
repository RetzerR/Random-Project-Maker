from flask import Flask, render_template
from randomg import give
app = Flask('app')


@app.route('/')
def hello_world():
  return render_template("index.html", project=give())

@app.route("/api/")
def api():
    return give()

app.run(host='0.0.0.0', port=8080)