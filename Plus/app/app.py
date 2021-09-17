from flask import Flask, jsonify
from flask_appbuilder import AppBuilder, SQLA
from models import Employee
from flask import request


app = Flask(__name__)

app.config.from_object("config")
db = SQLA(app)


@app.route('/')
def index():
    return 'hello!!'

@app.route('/employee/<string:username>', methods=['POST'])
def create(username: str):
    data = request.get_json()
    e = Employee()
    e.username = username
    e.email = data["email"]
    e.mobile = data["mobile"]
    e.title = data["position"]["title"]
    e.department = data["position"]["department"]
    db.session.add(e)
    db.session.commit()
    return jsonify(e.get())

@app.route('/employee/<string:username>', methods=['GET'])
def get(username: str):
    e = Employee.query.filter(Employee.username == username).first()
    return jsonify({}) if e is None else jsonify(e.get())

@app.route('/employee/<string:username>', methods=['PUT'])
def update(username: str):
    data = request.get_json()
    e = Employee.query.filter(Employee.username == username).first()
    e.email = data["email"]
    e.mobile = data["mobile"]
    e.title = data["position"]["title"]
    e.department = data["position"]["department"]
    return jsonify("success")

@app.route('/employee/<string:username>', methods=['DELETE'])
def delete(username: str):
    e = Employee.query.filter(Employee.username == username).delete()
    db.session.commit()
    return jsonify({
        "result": "Not exists"
    }) if e is None else jsonify({
        "result": "Delete Success"
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')