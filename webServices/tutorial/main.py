from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    name = 'Nohely, la más otaka'
    secret_message = True

    return render_template('index.html', username=name, secret_message=secret_message)


if __name__ == '__main__':
    app.run(debug=True, port=9000)
