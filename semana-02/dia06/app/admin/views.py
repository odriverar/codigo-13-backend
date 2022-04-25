from flask import render_template, redirect, url_for, session, flash

from . import admin

#Importamos los formularios
from app.forms import LoginForm, ProyectosForm

## para autenticacion de usuarios ##
import pyrebase
from app.auth_token import firebaseConfig

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
################################################################################

from app.firebaseCnn import db

@admin.route('/')
def index():
    if('token' in session):
        return render_template('admin/index.html')
    else:
        return redirect(url_for('admin.login'))

@admin.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    context = {
        'login_form': login_form
    }
    #### codigo para login de usuarios ####
    if login_form.validate_on_submit():
        usuarioData = login_form.usuario.data
        passwordData = login_form.password.data
        try:
            usuario = auth.sign_in_with_email_and_password(usuarioData, passwordData)
            dataUsuarioValido = auth.get_account_info(usuario['idToken'])
            print(dataUsuarioValido)
            session['token'] = usuario['idToken']
            return redirect(url_for('admin.index'))
        except:
            print('Usuario incorrecto')
            flash("Usuario o password invalido")
            
    return render_template('admin/login.html', **context)

@admin.route('/logout')
def logout():
    session.pop('token')
    return redirect(url_for('admin.login'))

@admin.route('/proyectos', methods=['GET', 'POST'])
def proyectos():
    if ('token' in session):
        colProyectos = db.collection('proyectos')
        ###### Formulario proyectos 
        proyectos_form = ProyectosForm()
        
        if proyectos_form.validate_on_submit():
            codigo = proyectos_form.codigo.data
            nombre = proyectos_form.nombre.data
            descripcion = proyectos_form.descripcion.data
            imagen = proyectos_form.imagen.data
            url = proyectos_form.url.data
            
            dataNuevoProyecto = {
                'codigo': codigo,
                'nombre': nombre,
                'descripcion': descripcion,
                'imagen': imagen,
                'url': url
            }

            colProyectos.document().set(dataNuevoProyecto)
        
        ###### Obtenemos los registros
        docProyectos = colProyectos.get()
        lstProyectos = []
        
        for doc in docProyectos:
            dicProyectos = doc.to_dict()
            lstProyectos.append(dicProyectos)
        
        context = {
            'proyectos': lstProyectos,
            'proyectos_form': proyectos_form
        }
        
        return render_template('admin/proyectos.html', **context)
    else:
        return redirect(url_for('admin.login'))