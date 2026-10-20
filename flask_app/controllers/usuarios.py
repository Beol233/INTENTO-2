from flask_app import app
from flask import render_template, request, redirect, flash, session
from flask_app.models.usuario import Usuario
from flask_bcrypt import Bcrypt 

bcrypt = Bcrypt(app)

@app.route("/")
def inicio():
    return render_template('index.html')



@app.route("/crear_usuario", methods=["POST"])
def crear_usuario():


    if not Usuario.validar_registro(request.form):
        print("Usuario Invalido")
        return redirect('/')


    pass_hasheado = bcrypt.generate_password_hash(
        request.form['password']
    ).decode('utf-8')

    datos_usuario_registro = {
        "nombre": request.form ['nombre'],
        "apellido": request.form ['apellido'],
        "email": request.form ['email'],
        "password": pass_hasheado
        
    }

    nuevo_id = Usuario.save(datos_usuario_registro)

    session['usuario_id'] = nuevo_id

    return redirect('/lista')


@app.route('/iniciar_sesion', methods=['POST'])
def iniciar_sesion():
    usuario = Usuario.get_by_email({'email': request.form['email_inicio_sesion']})
    if not usuario or not bcrypt.check_password_hash(usuario.password, request.form['password_inicio_sesion']):
        flash("E-mail o contraseña incorrectos", "inicio_sesion")
        return redirect('/')

    session['usuario_id'] = usuario.id
    session['nombre'] = usuario.nombre
    return redirect('/lista')


@app.route('/cerrar_sesion')
def cerrar_sesion():

    session.clear()
    return redirect('/')
