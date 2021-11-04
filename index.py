from flask import Flask, render_template
from flask_mysqldb import MySQL


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

#Mysql Connection
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASWWORD'] = 'luzabaza'
app.config['MYSQL_DB'] = 'registration'
mysql = MySQL(app)

# settings
app.secret_key = 'mysecretkey'


@app.route('/', strict_slashes=False)
def Index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM Users')
    data = cur.fetchall()
    return render_template('index.html', users = data)

@app.route('/registration', methods=['POST'])
def registration():
    if request.method == 'POST':
        Name = request.form['Name']
        Phone = request.form['Phone']
        Email = request.form['Email']
        Address = request.form['Address']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO Users (Name, Phone, Email, Address) VALUES (%s, %s, %s, %s)',
        (Name, Phone, Email, Address))
        mysql.connection.commit()
        flash('has been successfully registered')
        return redirect(url_for('Index'))


if __name__ == '__main__':
	app.run(host='0.0.0.0', port='5017', debug=True)
