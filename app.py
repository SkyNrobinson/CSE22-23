from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/Paul')
def Paul():
	return render_template('Paul.html')

@app.route('/Jacob')
def Jacob():
    return render_template('Jacob.html')

@app.route('/JohnN')
def JohnN():
    return render_template('JohnN.html')