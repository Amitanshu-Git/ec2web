from flask import Flask, jsonify, render_template

app = Flask(__name__)


@app.route('/')
def hello_sever():
    return "Hello I'm Sinu"


@app.route('/index')
def index_json():
    detail_dict = {"message": "Hello I'm Sinu",
            "School": "DAV and Public",
            "Hobby": "Ghar ke Kaam",
                   }
    return jsonify(detail_dict)


@app.route('/bisay')
def about_myself():
    return render_template('about.html')
