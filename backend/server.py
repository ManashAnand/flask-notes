from flask import Flask, request, jsonify
from flask import request
from markupsafe import escape
from flask_cors import CORS
import cv2
import io
import os

import numpy as np


app = Flask(__name__)
CORS(app)

@app.route("/")
def member():
    return {"member":["Member 1","Member 2"]}

@app.route("/<name>")
def hello(name):
    return f"Hello, {escape(name)}!"

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return {"member":["Login succesfull"]}
    


@app.route('/getImage', methods=['POST'])
def convertImg():
    try:
        # Ensure the 'img' folder exists in the current working directory
        img_folder = os.path.join(os.getcwd(), 'img')
        os.makedirs(img_folder, exist_ok=True)

        img_file = request.files['image']
        img_bytes = img_file.read()
        img_array = np.frombuffer(img_bytes, dtype=np.uint8)
        img_open = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

        # Convert to grayscale
        img_gray = cv2.cvtColor(img_open, cv2.COLOR_BGR2GRAY)

        # Save the grayscale image
        save_path = os.path.join(img_folder, "manash.jpg")
        img_save = cv2.imwrite(save_path, img_gray)

        return jsonify({"message": "Image uploaded and processed successfully"})
    except Exception as e:
        print(e)
        return jsonify({"error": "An error occurred during image upload"})



if __name__ == "__main__":
    app.run(debug=True)