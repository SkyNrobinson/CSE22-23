from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')
@app.route('JohnC')
def hello():
    return render_template('JohnC.html', JohnC)
