from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    title = 'IDGS804 - IntroFlask'
    listado = ['Paulobot', 'Karlabot','Lizbot','Pereira7']
    return render_template('index.html', title=title, listado=listado)

@app.route('/saludo1')
def saludo1():
    return render_template('saludo1.html')

@app.route('/saludo2')
def saludo2():
    return render_template('saludo2.html')

@app.route('/')
def home():
    return 'Hola Mundo'

@app.route('/hola')
def func():
    return 'Hola Mundo insano   -- Hola23'

@app.route('/user/<string:user>')
def user(user):
    return f'Hola Mundo {user}'


@app.route('/numero/<int:n>')
def numero(n):
    return f'El numero es {n}'

@app.route('/user/<int:id>/<string:username>')
def username(id, username):
    return f'<h1>Hola tu id es: {id}, y tu nombre es: {username}'


@app.route('/suma/<float:n1>/<float:n2>')
def suma(n1, n2):
    return f'<h1>La suma es: {n1 + n2}</h1>'

@app.route('/default')
@app.route('/default/<string:param>')
def func2(param='paulo'):
    return f'<h1>Hola {param}</h1>'



@app.route('/operas')
def operas():
    return '''
        <form>
        <label for="name"> Nombre: </label>
        <input type="text" id="name" name="name" required>
        </br>
        <label for="name"> Paterno: </label>
        <input type="text" id="name" name="name" required>
        </br>
        <label for="pass"> Password: </label>
        <input type="password" id="pass" name="pass">
        </br>
        <input type="submit" value="Enviar">
        </form>
'''

@app.route('/operasBase')
def Operasas():
    return render_template('operasBase.html')


@app.route('/resultado', methods=['GET'])
def resultado():
    n1 = request.args.get('numero1')
    n2 = request.args.get('numero2')
    return f'<h1>La suma es: {float(n1) + float(n2)}</h1>'

if __name__ == '__main__':
    app.run(debug=True)