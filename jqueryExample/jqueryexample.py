
from flask import Flask, jsonify, render_template, request
app = Flask(__name__)


@app.route('/_add_numbers')
def add_numbers():
    """Add two numbers server side, ridiculous but well..."""
    a = request.args.get('a', 0, type=int) #if no 'a', set default to 0
    b = request.args.get('b', 0, type=int)
    return jsonify(result=a + b) #the JSON respnse will be like {"result":42 }


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
   app.debug=True; 
   app.run()