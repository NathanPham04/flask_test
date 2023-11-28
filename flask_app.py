from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!<p>"

@app.route("/name")
def name():
    return "nathan"

@app.route("/coolKidsOnly")
def cool():
    return ["For", "Cool", "Kids", "Only"]


if __name__ == "__main__":
    print("Flask api demo running")
    app.run(debug=True)