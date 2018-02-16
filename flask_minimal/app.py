from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "Hello World!"


@app.route('/route1')
def my_function():
    return "Hello World from route1!"


@app.route('/int/<number>')
def numbers(number):
    print(number)
    return "The number is printed on console"

@app.route('/homepage')
def home_page():
	return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
