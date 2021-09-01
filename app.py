from flask import Flask, jsonify, redirect, request, render_template
from flask_sqlalchemy import SQLAlchemy
from config import DATABASE_URI
import os
import random
import string

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    'DATABASE_URL', DATABASE_URI)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
db.init_app(app)
db.create_all()


class URL(db.Model):
    __tablename__ = 'urls'
    shortened_url = db.Column(db.Text, primary_key=True)
    url = db.Column(db.Text, nullable=False)

    def __init__(self, url, shortened_url):
        self.url = url
        self.shortened_url = shortened_url


@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == "GET":
        return render_template('index.html')
    else:
        url_posted = False
        while not url_posted:
            short_url = ''.join(random.choices(string.ascii_letters, k=15))
            data = URL.query.filter_by(shortened_url=short_url)
            if data.count() == 0:
                url_posted = True
        url = URL(request.form["url"], short_url)
        db.session.add(url)
        db.session.commit()
        host = os.environ.get('BASE_HOST_URL', 'http://127.0.0.1:5000/')
        return render_template('index.html', host=host, url=url.shortened_url)


@app.route('/urls/')
def index():
    data = URL.query.all()
    response = [{"url": element.url, "shortened_url": element.shortened_url}
                for element in data]
    return jsonify({"data": response})


@app.route('/<string:url_id>/')
def redirect_to_url(url_id):
    url = URL.query.filter_by(shortened_url=url_id).first()
    if not url:
        return redirect('/')
    else:
        if url.url[0:4] == 'http':
            return redirect(url.url)
        else:
            return redirect(f'http://{url.url}')
