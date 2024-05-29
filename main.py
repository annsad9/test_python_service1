from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///material.db'

db = SQLAlchemy(app)
#БД
class Material(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    quantity = db.Column(db.Integer)

    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity


with app.app_context():
    db.create_all()
#запись данных
@app.route('/add_material', methods=['POST'])
def add_material():
    name = request.form['name']
    quantity = request.form['quantity']
    material = Material(name, quantity)
    db.session.add(material)
    db.session.commit()
    return{'success': 'Material added successfully'}

@app.route('/get_material/<int:id>')
def get_material(id):
    material = Material.query.get(id)
    if material:
        return jsonify({
            'id': material.id,
            'name': material.name,
            'quantity': material.quantity
        })
    else:
        return{'error': 'Material not found'}

if __name__=="__main__":
    app.run(host="0.0.0.0", debug=True)

#import requests as r
#res = requests.get(url = 'http://127.0.0.1:5000/get_material/1')
#res = requests.post(url = 'http://127.0.0.1:5000/add_material', data = {'name': 'name1', 'quantity':'quantity1'})