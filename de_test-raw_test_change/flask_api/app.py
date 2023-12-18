from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@db:5432/test_db'
db = SQLAlchemy(app)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    quantity = db.Column(db.Integer, default=0)
    


@app.route('/')
def index():
    return "Welcome to Flask API!"

@app.route('/items', methods=['GET'])
def get_items():
    items = Item.query.all()
    return jsonify([item.serialize for item in items])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

