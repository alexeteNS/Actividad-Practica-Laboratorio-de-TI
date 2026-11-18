from flask import Flask, render_template, request
import uuid

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/prestar-equipo', methods=['POST'])
def prestar_equipo():
    nombre = request.form.get('nombre')
    equipo = request.form.get('equipo')
    adeudos = request.form.get('adeudos')
    semestre = int(request.form.get('semestre'))

    if adeudos == 'Si':
        return render_template('index.html', aprobado=False, nombre=nombre, equipo=equipo,
                               motivo='Préstamo denegado: el estudiante tiene adeudos previos.')

    if equipo == 'Laptop de Pruebas' and semestre < 4:
        return render_template('index.html', aprobado=False, nombre=nombre, equipo=equipo,
                               motivo='Préstamo denegado: la Laptop de Pruebas requiere cursar 4.º semestre o superior.')

    folio = 'LAB-' + uuid.uuid4().hex[:8].upper()
    return render_template('index.html', aprobado=True, nombre=nombre, equipo=equipo, folio=folio)


if __name__ == '__main__':
    print('Servidor corriendo en: http://127.0.0.1:5000/')
    app.run(debug=True)
