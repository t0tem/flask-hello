from flask import Flask
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