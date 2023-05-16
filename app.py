from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')
@app.route('JohnC')
def hello(JohnC):
    return render_template('page.html', JohnC)
