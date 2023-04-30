from flask import Flask, request, jsonify
from detect import run

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def text():
    return "Hello Flutter"

@app.route('/predict', methods = ['POST'])
def predict():
    if request.method == "POST":
        file = request.files['file']
        file.save("test_4.jpg")
        
        data = run()
        print(data)

        return jsonify({'test' : data})

if __name__ == '__main__':
    app.run('0.0.0.0', port = 5000, debug = True)
