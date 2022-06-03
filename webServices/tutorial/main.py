from flask import Flask, render_template, request

app = Flask(__name__)


@app.before_request
def before_request():
    print("Antes de la petición")


@app.after_request
def after_request(response):
    print("Después de la petición")
    return response


@app.route('/')
def index():
    name = 'Nohely, la más otaka'
    secret_message = True

    return render_template('index.html', username=name,
                           secret_message=secret_message)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/usuario/<last_name>/<name>')
def user(last_name, name):
    return 'Hola, ' + last_name + name


# Esta función sirve para mandar datos desde los queries (el link)
# por ejemplo en este caso podría quedar así:
# localhost:9000/datos?nombre=nohely&curso=python
@app.route('/datos')
def datos():
    nombre = request.args.get('nombre', '')
    curso = request.args.get('curso', '')
    return 'Listado de datos: ' + nombre + ' ' + curso


if __name__ == '__main__':
    app.run(debug=True, port=9000)
