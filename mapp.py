from flask import Flask, render_template

app = Flask(__name__)


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


if __name__ == '__main__':
    app.run(debug=True)
