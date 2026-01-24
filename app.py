from flask import Flask, render_template, request
import forms
from flask_wtf.csrf import CSRFProtect
import math

app = Flask(__name__)
app.secret_key = 'clave_secreta'
csfr=CSRFProtect()


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

@app.route('/operasBase', methods=['GET', 'POST'])
def operasBase():
    resultado = None

    if request.method == 'POST':
        n1 = float(request.form.get('numero1'))
        n2 = float(request.form.get('numero2'))
        operacion = request.form.get('operacion')

        if operacion == 'suma':
            resultado = n1 + n2
        elif operacion == 'resta':
            resultado = n1 - n2
        elif operacion == 'multiplicacion':
            resultado = n1 * n2
        elif operacion == 'division':
            resultado = n1 / n2 if n2 != 0 else "No se puede dividir entre 0"

    return render_template('operasBase.html', resultado=resultado)

@app.route('/resultado', methods=['POST'])
def resultado():
    n1 = request.form.get('numero1')
    n2 = request.form.get('numero2')
    return f'<h1>La suma es: {float(n1) + float(n2)}</h1>'


@app.route('/distancia', methods=['GET', 'POST'])
def distancia():
    resultado = None
    if request.method == 'POST':
        x1 = float(request.form.get('x1'))
        y1 = float(request.form.get('y1'))
        x2 = float(request.form.get('x2'))
        y2 = float(request.form.get('y2'))
        resultado = math.sqrt((x2 - x1)**2+(y2 - y1)**2)

    return render_template('distancia.html', resultado=resultado)

@app.route('/alumnos', methods=['GET', 'POST'])
def alumnos():
    matricula = 0
    nombre = ''
    apellido = ''
    correo = ''
    alumno_class=forms.UserForm(request.form)
    if request.method == 'POST' and alumno_class.validate():
        matricula = alumno_class.matricula.data
        nombre = alumno_class.nombre.data
        apellido = alumno_class.apellido.data
        correo = alumno_class.correo.data
    return render_template('alumnos.html', form=alumno_class, matricula=matricula, nombre=nombre, apellido=apellido, correo=correo)
                          
if __name__ == '__main__':
    csfr.init_app(app)
    app.run(debug=True)
    
    

