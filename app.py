from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://username:password@localhost:5342/urls'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.app_context().push()
db = SQLAlchemy()
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
        return render_template('index.html', url=url.shortened_url)


if __name__ == '__main__':
    app.run()
