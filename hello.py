from flask import Flask, request, jsonify, abort, redirect, url_for, render_template
import numpy as np
from sklearn.externals import joblib

app = Flask(__name__)

knn = joblib.load('knn.pkl') 

@app.route('/')
def hello_world():
    print(1+2)
    return '<h1>Hello, my very best friend!!!</h1>'

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    username = float(username) * float(username)
    return 'User %s' % username

def mean(nums):
    return float(sum(nums)) / max(len(nums), 1)

@app.route('/avg/<nums>')
def avg(nums):
    nums = nums.split(',')
    nums = [float(num) for num in nums]
    nums_mean = mean(nums)
    print(nums_mean)
    return str(nums_mean)

@app.route('/iris/<param>')
def iris(param):

    param = param.split(',')
    param = [float(i) for i in param]

    print(param)

    param = np.array(param).reshape(1,-1)
    predict = knn.predict(param)
    return str(predict)


@app.route('/show_image')
def show_me_image(): # not necessary the same name as app.route
    return '<img src="/static/setosa.jpg" alt="setosa">'

@app.route('/badrequest400')
def bad_request():
    return abort(400)

@app.route('/iris_post', methods=['POST'])
def add_message():
    try:
        content = request.get_json()

        param = content['flower'].split(',')
        param = [float(i) for i in param]

        param = np.array(param).reshape(1,-1)
        predict = knn.predict(param)

        predict = {'class': str(predict[0])}
    except:
        return redirect(url_for('bad_request'))

    return jsonify(predict)

from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

app.config.update(dict(
    SECRET_KEY="powerful secretkey",
    WTF_CSRF_SECRET_KEY="a csrf secret key"
))

class MyForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])

@app.route('/submit', methods=('GET', 'POST'))
def submit():
    form = MyForm()
    if form.validate_on_submit():
        print(form.name)
        return(str(form.name))
    return render_template('submit.html', form=form)
