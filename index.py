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

@app.route('/pets')
def pets():
	return render_template('pets.html')


if __name__ == '__main__':
	app.run(host='0.0.0.0', port='5000', debug=True)
