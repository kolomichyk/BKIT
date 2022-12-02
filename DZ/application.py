from flask import Flask
import fib

app = Flask('Fibonachi')


@app.route('/')
def welcome():
    return "Hello, this is Fibonachi application"

@app.route('/<int:n>')
def index(n):
    return str(list(fib.Get_Fib_n(n*2)))

@app.errorhandler(404)
def page_not_found(e):
    return "Try to enter a number!"