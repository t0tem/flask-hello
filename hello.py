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

@app.route('/iris/<param>')
def iris(param):

    param = param.split(',')
    param = [float(i) for i in param]

    print(param)

    import numpy as np
    from sklearn import datasets
    iris = datasets.load_iris()
    iris_X = iris.data
    iris_y = iris.target
    np.unique(iris_y)

    # Split iris data in train and test data
    # A random permutation, to split the data randomly
    np.random.seed(0)
    indices = np.random.permutation(len(iris_X))
    iris_X_train = iris_X[indices[:-10]]
    iris_y_train = iris_y[indices[:-10]]
    iris_X_test  = iris_X[indices[-10:]]
    iris_y_test  = iris_y[indices[-10:]]
    # Create and fit a nearest-neighbor classifier
    from sklearn.neighbors import KNeighborsClassifier
    knn = KNeighborsClassifier()
    knn.fit(iris_X_train, iris_y_train) 
    KNeighborsClassifier(algorithm='auto', leaf_size=30, metric='minkowski',
    metric_params=None, n_jobs=None, n_neighbors=5, p=2,
    weights='uniform')
    knn.predict(iris_X_test)

    param = np.array(param).reshape(1,-1)
    predict = knn.predict(param)
    return str(predict)