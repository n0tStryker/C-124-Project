from flask import Flask, jsonify, request

app = Flask(__name__)

contact = {

    'id': tasks[-1]['id'] + 1,
    'Name': request.json['Name'],
    'Contact': request.json.get('Contact', ""),
    'done': False
}

@app.route("/add-data", methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message": "Please provide the data!"
        },400)

    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['number'],
        'description': request.json.get('name', ""),
        'done': False
    }
    tasks.append(task)
    return jsonify({
        "status":"success",
        "message": "Task added succesfully!"
    })