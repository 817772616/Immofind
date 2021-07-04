from flask import Flask
from flask import render_template
import json


app = Flask(__name__)
MAX_PRICE = 800


@app.route('/')
def index():
    with open('static/output.json', 'r') as inp:
        data = json.loads(inp.read())

    return render_template('main.html', data=data, max=MAX_PRICE)


if __name__ == '__main__':
    app.run()
