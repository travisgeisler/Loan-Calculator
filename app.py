from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', pageTitle='Flask Server Home Page')

@app.route('/travis')
def travis():
    return render_template('travis.html', pageTitle='About Travis')


if __name__ == '__main__':
    app.run(debug=True)
