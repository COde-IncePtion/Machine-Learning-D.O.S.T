from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World!"

@app.route("/profile")
def profile():
    return "you r in profile section"


if __name__ == "__main__":
    app.run()
