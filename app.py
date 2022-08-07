from flask import Flask
from flask import render_template

from models import *

app = Flask(__name__)
init_db()
session = session()


# Output all posts
@app.route('/')
def index():
    posts = session.query(Posts).all()
    return render_template('index.html', posts=posts)


if __name__ == '__main__':
    app.run(debug=True)
