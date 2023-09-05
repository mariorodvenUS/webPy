from flask import Flask,render_template, request, redirect

app = Flask(__name__)

# INDEX
@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')
# NOTICIAS
@app.route('/noticias', methods=['POST', 'GET'])
def noticias():
    return render_template('noticias.html')

# QUIÉNES SOMOS
@app.route('/quienes_somos', methods=['POST','GET'])
def quienes_somos():
    return render_template('quienes-somos.html')

# CURSOS (incompleto)
@app.route('/cursos', methods=['POST','GET'])
def cursos():
    return render_template('cursos.html')

    #DISEÑO E IMPRESION 3D
@app.route('/cursos/diseno', methods=['POST','GET'])
def diseno():
    return render_template('diseno.html')

    #PYTHON
@app.route('/cursos/python', methods=['POST','GET'])
def python():
    return render_template('python.html')

    #ROBOTICA
@app.route('/cursos/robotica', methods=['POST','GET'])
def robotica():
    return render_template('robotica.html')

# IMPRESIÓN (incompleto)
@app.route('/impresion', methods=['POST','GET'])
def impresion():
    return render_template('construccion.html')

if __name__ == "__main__":
        app.run(debug=True)
