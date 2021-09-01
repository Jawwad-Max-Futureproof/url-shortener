from flask import Flask, jsonify, request, render_template
from flask_sqlalchemy import SQLAlchemy
from config import DATABASE_URI
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    'DATABASE_URL', DATABASE_URI)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
db.init_app(app)
db.create_all()


class URL(db.Model):
    __tablename__ = 'urls'
    shortened_url = db.Column(db.String(5000), primary_key=True)
    url = db.Column(db.String(5000), nullable=False)

    def __init__(self, url, shortened_url):
        self.url = url
        self.shortened_url = shortened_url


@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == "GET":
        return render_template('index.html')
    else:
        url = URL(request.form["url"], request.form["url"])
        db.session.add(url)
        db.session.commit()
        return render_template('index.html', url=url.shortened_url)


@ app.route('/urls')
def index():
    data = URL.query.all()
    response = [{"url": element.url, "shortened_url": element.shortened_url}
                for element in data]
    return jsonify({"data": response})
