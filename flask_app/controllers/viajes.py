from flask_app import app
from flask import render_template, session, redirect, request
from flask_app.models.usuario import Usuario
from flask_app.models.viaje import Viaje
from datetime import date

@app.route('/lista')
def lista():
    if 'usuario_id' not in session:
        return redirect('/')

    viajes = Viaje.get_all()
    return render_template('lista.html', viajes=viajes)


@app.route('/nuevo')
def mostrar_nuevo():
    if 'usuario_id' not in session:
        return redirect('/')

    return render_template('crear.html')


@app.route('/crear_viaje', methods=['POST'])
def crear_viaje():
    if 'usuario_id' not in session:
        return redirect('/')

    destino = request.form.get('destino', '').strip()
    fecha_inicio = request.form.get('fecha_inicio', '')
    fecha_fin = request.form.get('fecha_fin', '')
    itinerario = request.form.get('itinerario', '').strip()

    if not destino or not fecha_inicio or not fecha_fin or not itinerario:
        return redirect('/nuevo')

    if len(itinerario) > 40:
        return redirect('/nuevo')

    try:
        inicio = date.fromisoformat(fecha_inicio)
        fin = date.fromisoformat(fecha_fin)
    except ValueError:
        return redirect('/nuevo')

    if inicio < date.today():
        return redirect('/nuevo')

    if fin < inicio:
        return redirect('/nuevo')

    datos = {
        'destino': destino,
        'fecha_inicio': fecha_inicio,
        'fecha_fin': fecha_fin,
        'itinerario': itinerario
    }

    viaje_id = Viaje.save(datos)

    if not viaje_id:
        return redirect('/nuevo')

    datos_vinculo = {
        'usuario_id': session['usuario_id'],
        'viaje_id': viaje_id
    }

    Viaje.vincular_usuario(datos_vinculo)

    return redirect('/lista')

@app.route('/ver/<int:id>')
def ver_viaje(id):
    if 'usuario_id' not in session:
        return redirect('/')

    viaje = Viaje.get_one({'id': id})

    if viaje is None:
        return redirect('/lista')

    return render_template('ver.html', viaje=viaje)


@app.route('/actualizar_viaje/<int:id>', methods=['POST'])
def actualizar_viaje(id):
    if 'usuario_id' not in session:
        return redirect('/')

    destino = request.form.get('destino', '').strip()
    fecha_inicio = request.form.get('fecha_inicio', '')
    fecha_fin = request.form.get('fecha_fin', '')
    itinerario = request.form.get('itinerario', '').strip()

    if not destino or not fecha_inicio or not fecha_fin or not itinerario:
        return redirect(f'/editar/{id}')

    if len(itinerario) > 40:
        return redirect(f'/editar/{id}')

    try:
        inicio = date.fromisoformat(fecha_inicio)
        fin = date.fromisoformat(fecha_fin)
    except ValueError:
        return redirect(f'/editar/{id}')

    if inicio < date.today() or fin < inicio:
        return redirect(f'/editar/{id}')

    datos = {
        'id': id,
        'destino': destino,
        'fecha_inicio': fecha_inicio,
        'fecha_fin': fecha_fin,
        'itinerario': itinerario
    }

    Viaje.update(datos)

    return redirect('/lista')


@app.route('/editar/<int:id>')
def editar_viaje(id):
    if 'usuario_id' not in session:
        return redirect('/')

    viaje = Viaje.get_one({'id': id})

    if viaje is None:
        return redirect('/lista')

    return render_template('edit.html', viaje=viaje)


@app.route('/eliminar/<int:id>')
def eliminar_viaje(id):
    Viaje.delete({'id':id})
    return redirect('/lista')


