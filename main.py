from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

db = SQLAlchemy(app)


# БД
class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    place = db.Column(db.String(50))
    material = db.Column(db.String(50))
    quantity = db.Column(db.Integer)

    def __init__(self, name, place, material, quantity):
        self.name = name
        self.place = place
        self.material = material
        self.quantity = quantity


with app.app_context():
    db.create_all()


# запись данных
@app.route('/add_data', methods=['POST'])
def add_data():
    name = request.form['name']
    place = request.form['place']
    material = request.form['material']
    quantity = request.form['quantity']
    data = Data(name, place, material, quantity)
    db.session.add(data)
    db.session.commit()
    return {'success': 'Material added successfully'}


@app.route('/get_data/<name>')
def get_data(name):
    data = Data.query.get(name)
    if data:
        return jsonify({
            'id': data.id,
            'name': data.name,
            'place': data.place,
            'material': data.name,
            'quantity': data.quantity
        })
    else:
        return {'error': 'Name not found'}


@app.route('/del_data/<int:id>',  methods=['DELETE'])
def del_data(id):
    id = Data.query.get(id)
    if id:
        db.session.delete(id)
        db.session.commit()
        return jsonify({'success': 'ID deleted successfully'})
    else:
        return {'error': 'ID not found'}

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

#import requests
# res = requests.get(url = 'http://127.0.0.1:5000/get_data/1')
# res = requests.post(url = 'http://127.0.0.1:5000/add_data', data = {'name': 'Ivan', 'place':'dom 33','material': 'tiles','quantity':'49'})
# res = requests.delete(url = 'http://127.0.0.1:5000/del_data/1')