from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)

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

@app.route('/edit')
def edit():
    return 'edit'

@app.route('/delete/<string:id>')
def delete_user(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM Users WHERE id = {0}'.format(id))
    mysql.connection.commit()
    flash('User Successfully Removed')
    return redirect(url_for('Index'))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000', debug=True)
