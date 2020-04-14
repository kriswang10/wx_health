import config
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, Blueprint

app = Flask(__name__)
app.config.from_object(config)

db = SQLAlchemy(app)
db.create_all()


@app.route('/')
def hello():
    return 'hello'


if __name__ == '__main__':
    app.run(debug=True)
