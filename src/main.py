from re import DEBUG
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask import request
from scrapper import Scrapper

app = Flask(__name__, template_folder='../templates',
            static_url_path='', static_folder='../static')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123@localhost:5432/news'
app.config['SECRET_KEY'] = 'thisismyflasksecretkey'

db = SQLAlchemy(app)


class News(db.Model):
    __tablename__ = 'news'

    id = db.Column(db.Integer, primary_key=True)
    source = db.Column(db.String())
    sourcelink = db.Column(db.String())
    title = db.Column(db.String())
    subtitle = db.Column(db.String())
    time = db.Column(db.String())
    paragraph = db.Column(db.String())

    def __init__(self, source, sourcelink, title, subtitle, time, paragraph):
        self.source = source
        self.sourcelink = sourcelink
        self.title = title
        self.subtitle = subtitle
        self.time = time
        self.paragraph = paragraph

    def add(self):
        db.session.add(self)
        db.session.commit()
        pass


@app.route('/', methods=['GET', 'POST'])
def main():
    query = request.form.get('text-field')

    if not query:
        return render_template('search.html', query=query)

    return render_template('search.html', query=query, data=scrap(query))


def scrap(query):
    scrapper = Scrapper()
    results = scrapper.get_data(query)

    for result in results:
        news = News(
            title=result['title'],
            subtitle=result['subtitle'],
            source=result['source'],
            sourcelink=result['sourcelink'],
            time=result['time'],
            paragraph=result['paragraph']
        )
        news.add()

    return results


db.drop_all()
db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
