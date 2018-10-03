from flask import Flask, render_template, jsonify


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