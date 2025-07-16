from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Willkommen auf der Startseite!"

@app.route('/hello')
def hello():
    return "Hallo von Flask!"

if __name__ == "__main__":
    app.run(debug=True)