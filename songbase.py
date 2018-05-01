from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    # return "hello world"
    return render_template('index.html')


@app.route('/users/<string:username>')
def users(username):
    #return "<h1>Hello<h1> %s" % username
    return render_template('user.html', username=username)


@app.route('/user')
def user():
    return "This is the page for users"


if __name__ == '__main__':
    app.run()
