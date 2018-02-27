from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'JR'}

    posts = [
        {
            'title': {'main': 'I hate Python', 'sub': 'this is a sad story'},
            'body': 'Python can do every thing. However, it is very hard.'
        },
        {
            'title': {'main': 'I love Python', 'sub': 'this is a happy story'},
            'body': 'Python can do every thing. However, it is very easy.'
        },

        {
            'title': {'main': 'I love C#'},
            'body': 'c# can do some thing, and it is very easy!'
        }
    ]

    return render_template('index.html', user=user, posts=posts, title='A Title')


app.run()