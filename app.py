from flask import Flask, render_template, request, redirect, url_for
from flask_cors import CORS
from model import create_posts, get_posts, update_post, delete_post

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        post = request.form.get('post')
        create_posts(name, post)
        return redirect(url_for('index'))

    posts = get_posts()
    return render_template('index.html', posts=posts)

@app.route('/update', methods=['POST'])
def update():
    post_id = request.form.get('post_id')
    name = request.form.get('name')
    post = request.form.get('content')
    update_post(post_id, name, post)
    return redirect(url_for('index'))

@app.route('/delete/<int:post_id>', methods=['POST'])
def delete(post_id):
    delete_post(post_id)
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
