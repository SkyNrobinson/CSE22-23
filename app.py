from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')
@app.route('/JohnN')
def JohnN():
    return render_template('JohnN.html')
