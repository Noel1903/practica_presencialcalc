from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
@app.route("/")
def index():
    return "Backend"


if __name__ == "__main__":
    app.run(threaded=True, port=5000, debug=True)
