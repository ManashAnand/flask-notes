from flask import Flask, request, jsonify
from flask import request
from markupsafe import escape
from flask_cors import CORS
import cv2
import io
import os
import uuid
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
    


@app.route('/grayscale', methods=['POST'])
def grayscale():
    unique_id = uuid.uuid4()
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
        save_path = os.path.join(img_folder, f"manash_{unique_id}.jpg")
        img_save = cv2.imwrite(save_path, img_gray)

        return jsonify({"message": "Image uploaded and processed successfully"})
    except Exception as e:
        print(e)
        return jsonify({"error": "An error occurred during image upload"})

@app.route('/resize', methods=['POST'])
def resize():
    
    unique_id = uuid.uuid4()
    try:
        img_folder = os.path.join(os.getcwd(), 'img_resize')
        os.makedirs(img_folder, exist_ok=True)
        
        img_file = request.files['image']
        height = int(request.form['height'])
        width = int(request.form['width'])

        print(height)
        print(width)
        img_bytes = img_file.read()
        img_array = np.frombuffer(img_bytes, dtype=np.uint8)
        img_open = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        if height > 0 and width > 0:
            img_resize = cv2.resize(img_open, (width, height))
        # img_resize = cv2.resize(img_open,(height,width))
        
            save_path = os.path.join(img_folder, f"manash_{unique_id}.jpg")
            img_save = cv2.imwrite(save_path, img_resize)
        
        return jsonify({"message": "Image resize to 256 height and 256 width"})
    except Exception as e:
        print(e)
        return jsonify({"error": "An error occurred during image upload"})
    
    
@app.route('/rotateAngle', methods=['POST'])
def flip():
    print("working")
    unique_id = uuid.uuid4()
    try:
        img_folder = os.path.join(os.getcwd(), 'img_flip')
        os.makedirs(img_folder, exist_ok=True)
        
        print(request.form)
        print(request.files)
        
        img_file = request.files['image']
        angle = int(request.form['rotate'])
        print(angle)
        
        img_bytes = img_file.read()
        img_array = np.frombuffer(img_bytes, dtype=np.uint8)
        img_open = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        
        img_flip = cv2.flip(img_open,angle)
    
        save_path = os.path.join(img_folder, f"manash_{unique_id}.jpg")
        img_save = cv2.imwrite(save_path, img_flip)
        
        return jsonify({"message": "image flipped"})
    except Exception as e:
        print(e)
        return jsonify({"error": "An error occurred during image upload"})
    

if __name__ == "__main__":
    app.run(debug=True)