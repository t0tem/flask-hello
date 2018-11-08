from flask import Flask
app = Flask(__name__)

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