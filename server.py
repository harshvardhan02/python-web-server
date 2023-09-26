from flask import Flask, render_template, jsonify
from controllers.features import get_features_name, get_fruits, users
from controllers.home import get_name
from controllers.lambda_page import get_page_lambda
from controllers.numpy import get_page_numpy
from controllers.pandas import get_page_pandas

app = Flask(__name__)

@app.route("/")
def hello_world(name=get_name()):
    return render_template('index.html', name=name)

@app.route("/features")
def features(name=get_features_name(), fruits=get_fruits(), users=users()):
    return render_template('features.html', name=name, fruits=fruits, users=users)

@app.route("/lambda")
def lambdaPage(name=get_page_lambda()):
    return render_template('lambda.html', name=name)

@app.route("/numpy")
def numpy(name=get_page_numpy()):
    return render_template('numpy.html', name=name)

@app.route("/pandas")
def pandas(name=get_page_pandas()):
    return render_template('pandas.html', name=name)

@app.route("/api/users", methods=['GET'])
def user():
    data = {'name': 'Harshvardhan', 'age': 27, 'skills': ['Python', 'JavaScript', 'React']}
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)
