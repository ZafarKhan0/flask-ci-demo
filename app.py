from flask import Flask
import os


app = Flask(__name__)


@app.route('/')
def home():
    return "Hello, CI/CD!"


if __name__ == '__main__':
    app.run(debug=os.getenv('FLASK_DEBUG', 'False').lower() == 'true')