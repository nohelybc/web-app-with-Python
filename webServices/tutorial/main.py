from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "<h1>Hola gente linda de internet (desde mi servidor de Flask! :D)</h1>"


if __name__ == '__main__':
    app.run(debug=True, port=9000)
