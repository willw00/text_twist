from flask import Flask, request, render_template, jsonify
from random import sample
from collections import OrderedDict
import json

# initilize flask
app = Flask(__name__)

subwords = []
with open('subwords.json', 'r') as f:
    for line in f:
        subwords.append(json.loads(line))

# setup the route
@app.route('/hello')
def hello():
    return "Hello, World!"

@app.route('/', methods=['GET', 'POST'])
def home():
    subs = sample(subwords, 1)[0]['subwords']
    subs = OrderedDict(sorted(subs.items()))
    print subs
    if request.method == 'POST':
        return subs
    return render_template('index.html', subs=subs)

# run the server
if __name__ == '__main__':
    app.run(debug=True)