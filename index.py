from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/about us')
def about_us():
	return render_template('About_us.html')

@app.route('/connections')
def connections():
	return render_template('connections.html')

@app.route('/contac')
def contac():
	return render_template('contac.html')

if __name__ == '__main__':
	app.run(debug=True)
