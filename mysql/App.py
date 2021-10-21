from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
	return 'welcome'

@app.route('/registration')
def registration():
	return 'registration'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000', debug=True)
