from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/books/<int:id>')
def get_book(id):
    book = {
        "id": id,
        "title": "Flask API Development Cookbook",
        "author": "Steven F, Lott",
        "ppp": "123456"
    }
    return jsonify(book)

if __name__=="__main__":
    app.run(host="0.0.0.0",debug=True)