from flask import Flask, current_app, request, jsonify
import io
import model # import the model
import base64
import logging

app = Flask(__name__)
@app.route('/', methods=['POST'])
def predict():
    """With the model loaded, create a web server that can accept base64 encoded images using flask."""
    data = {}
    try:
        data = request.get_json()['data']
    except Exception:
        return jsonify(status_code='400', msg='Bad Request'), 400

    data = base64.b64decode(data)

    image = io.BytesIO(data)
    predictions = model.predict(image)
    current_app.logger.info('Predictions: %s', predictions)
    return jsonify(predictions=predictions)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)

