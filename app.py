from flask import Flask, request, jsonify
from flask_restful import Api
from tensorflow import keras
import numpy as np

app = Flask(__name__)
app
api = Api(app)
model = keras.models.load_model("model.h5")
@app.route('/api/classify/')
def test():
    x = np.array(request.args["img"].split(",")).astype(int).reshape(1,28,28)
    predictions = list(model.predict(x)[0].astype(np.int32))
    return jsonify(int(np.argmax(predictions)))

if __name__ == "__main__":
    app.run(port=5000)
