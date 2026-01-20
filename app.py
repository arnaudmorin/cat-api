import os
import random
from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route('/cat')
def cat():
    return pick('cats')

@app.route('/dog')
def dog():
    return pick('dogs')

def pick(what):
    gifs = [f for f in os.listdir(what) if f.endswith('.gif')]
    if not gifs:
        return "Error", 404
    return send_from_directory(what, random.choice(gifs), mimetype='image/gif')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=False)
