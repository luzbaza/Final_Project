from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/about us')
def about_us():
	return 'about us yes!'

@app.route('/connections')
def connections():
	return 'connections'

@app.route('/contac')
def contac():
	return 'contac'

if __name__ == '__main__':
	app.run(debug=True)