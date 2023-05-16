from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hello CSE - Get ready to rock and roll with Github! Maddix was here!!!'
