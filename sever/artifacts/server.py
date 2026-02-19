from flask import Flask, request, jsonify
from flask_cors import CORS
import util

app = Flask(__name__)

# Increase upload size (important for big images)
app.config['MAX_CONTENT_LENGTH'] = 32 * 1024 * 1024   # 32 MB

# Enable CORS for all routes
CORS(app)

@app.route('/classify_image', methods=['POST'])
def classify_image():
    # Check if data exists
    if 'image_data' not in request.form:
        return jsonify({"error": "No image_data found"}), 400

    image_data = request.form['image_data']

    try:
        result = util.classify_image(image_data)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    print("Starting Python Flask server for Sports Celebrity Image Recognition")
    util.load_saved_artifacts()
    app.run(host='0.0.0.0', port=5000, debug=True)
