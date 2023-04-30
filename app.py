from flask import Flask, request, jsonify
from detect import run

app = Flask(__name__)


@app.route('/predict', methods = ['POST'])
def predict():
    if request.method == "POST":
        file = request.files['file']
        file.save("test_4.jpg")

        return jsonify({'test' : run()})

if __name__ == '__main__':
    app.run()