from flask import Flask, render_template, jsonify, request
from backend.models import Todo
import backend.database


app = Flask(__name__,
            static_folder = "./dist/static",
            template_folder = "./dist")

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template("index.html")

@app.route('/api/about')
def about():
    response = {
        'message': 'This is About API Message!!!'
    }
    return jsonify(response)

@app.route('/api/todos', methods=['GET', 'POST'])
def todos():
    response = {}

    try:
        if request.method == 'GET':
            todos = backend.database.selectAllTodo()
            print(todos)
            response['todos'] = [todo.to_dict() for todo in todos]
        else:
            body = request.json['body']
            todo = Todo(body)
            print(todo)
            # 登録
            backend.database.insertTodo(todo)

        response['message'] = 'Success.'
    except:
        import traceback
        traceback.print_exc()
        response['message'] = 'Database Error.'

    return jsonify(response)

@app.route('/api/todo/<int:id>', methods=['DELETE'])
def todo(id):
    response = {}

    try:
        if request.method == 'DELETE':
            backend.database.deleteTodo(id)

        response['message'] = 'Success.'
    except:
        import traceback
        traceback.print_exc()
        response['message'] = 'Database Error.'
    
    return jsonify(response)


if __name__ == "__main__":
    app.run("0.0.0.0", debug=True)
