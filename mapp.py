from flask import Flask, render_template
from flask import url_for, session, logging, redirect, flash
from flask_mysqldb import MySQL
from passlib.hash import sha256_crypt
from mforms import RegisterForm
from flask import request

app = Flask(__name__)


# MySQL Configurations
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root123'
app.config['MYSQL_DB'] = 'flask_app'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)


@app.route('/')
def index():
    return render_template('index.html')


articles_data = [
            {'id': 1,
             'title': 'First Post',
             'author': 'Kishore',
             'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Animi asperiores culpa cum deleniti dolore fugiat, in iure laborum nesciunt nostrum quia quod voluptatibus. Aut eos fuga maxime, molestiae odio vel!'
             },
             {'id': 2,
             'title': 'Another Post',
             'author': 'Kishore',
             'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Animi asperiores culpa cum deleniti dolore fugiat, in iure laborum nesciunt nostrum quia quod voluptatibus. Aut eos fuga maxime, molestiae odio vel!'
             },
            ]


@app.route('/articles/')
def articles():
    return render_template('articles.html', articles=articles_data)


@app.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        username = form.username.data
        email = form.email.data
        pwd = sha256_crypt.encrypt(form.password.data)

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users(username, email, password) VALUES(%s, %s, %s)", (username, email, pwd))
        mysql.connection.commit()
        cur.close()

        flash("%s Registered" % username, 'success')

        return redirect(url_for('index'))
    return render_template('registration.html', form=form)


if __name__ == '__main__':
    app.secret_key = 'secret123'
    app.run(debug=True)
