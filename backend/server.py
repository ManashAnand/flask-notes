from flask import Flask
from flask import request
from markupsafe import escape

from flask_cors import CORS

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


if __name__ == "__main__":
    app.run(debug=True)