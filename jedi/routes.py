#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = '@britodfbr'

from jedi import app, database, bcrypt
from jedi.models import Usuario, Post
from jedi.forms import FormCriarConta, FormLogin, FormEditarPerfil, FormCriarPost
from flask import render_template, url_for, request, flash, redirect, abort
from flask_login import login_user, logout_user, current_user, login_required
from pathlib import Path
from PIL import Image
from unidecode import unidecode
import datetime as dt
import secrets
import ast


@app.route('/login', methods=['GET', 'POST'])
def login():
    form_login = FormLogin()
    form_criar_conta = FormCriarConta()
    if form_login.validate_on_submit() and 'submit_login' in request.form:
        usuario = Usuario.query.filter_by(email=form_login.email.data).first()
        if usuario and bcrypt.check_password_hash(usuario.password, form_login.password.data):
            login_user(usuario, remember=form_login.lembrar_dados.data)  # Efetivar login
            flash(f'Login realizado com sucesso: {form_login.email.data}!', 'alert-success')

            next_page = request.args.get('next')
            if next_page:
                return redirect(next_page)
            return redirect(url_for('home'))
        else:
            flash(f'Login ou Senha incorretos', 'alert-danger')

    if form_criar_conta.validate_on_submit() and 'submit_criar_conta' in request.form:
        usuario = Usuario(username=form_criar_conta.username.data,
                          password=bcrypt.generate_password_hash(form_criar_conta.password.data),
                          email=form_criar_conta.email.data)
        database.session.add(usuario)
        database.session.commit()
        flash(f'Conta criada com sucesso: {form_criar_conta.email_confirmation.data}', 'alert-success')
        return redirect(url_for('home'))
    return render_template('login.html', form_login=form_login, form_criar_conta=form_criar_conta)


@app.route('/sobre-nos')
def hello_world():
    return '''<center>
    <H1>Junta Especializada de Desenvolvimento e Inovação (JEDI)</H1>
        <a href="/">
            <img src="img/jedi_logo0.png" />
            HOME
        </a>
    </center>
    '''


@app.route('/index')
def index():
    posts = Post.query.order_by(Post.id.desc())
    return render_template('index.html', posts=posts)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/contato')
def contato():
    return render_template('contato.html')


@app.route('/usuarios')
@login_required
def usuarios():
    # lista_usuarios = Usuario.query.all()    # Todos os usuários
    # lista_usuarios = Usuario.query.order_by(Usuario.username.desc())    # Todos os usuários em ordem reversa
    lista_usuarios = Usuario.query.order_by(Usuario.username)    # Todos os usuários em ordem alfabetica
    return render_template('usuarios.html', lista_usuarios=lista_usuarios)


@app.route('/sair')
@login_required
def logout():
    logout_user()
    flash(f'Logout com sucesso!', 'alert-success')
    return redirect(url_for('home'))


@app.route('/perfil')
@login_required
def perfil():
    foto_perfil = url_for('static', filename=f'foto_perfil/{current_user.foto}')
    content = {
        'foto_perfil': foto_perfil,
    }
    return render_template('perfil.html', **content)


def save_img(image, size: tuple = None):
    size = size or (400, 400)
    filename = Path(app.root_path).joinpath('static/foto_perfil', image.filename)
    filename = filename.with_name(
        # unidecode(f"{filename.stem}-{secrets.token_hex(8)}{filename.suffix}").casefold().replace(' ', '_')
        unidecode(f"{dt.datetime.now().timestamp()}-{filename.stem}{filename.suffix}").casefold().replace(' ', '_')
    )
    thumb = Image.open(image)
    thumb.thumbnail(size)
    thumb.save(filename)
    return filename.name


def atualizar_cursos(form):
    result = []
    for campo in form:
        if campo.data:
            if 'curso_' in campo.name:
                result.append(campo.label.text)
    return ';'.join(result) if result else 'Não Informado'


@app.route('/perfil/editar', methods=['GET', 'POST'])
@login_required
def perfil_editar():
    form = FormEditarPerfil()
    if form.validate_on_submit():
        current_user.email = form.email.data
        current_user.username = form.username.data
        if form.foto_perfil.data:
            image_name = save_img(form.foto_perfil.data)
            print(image_name)
            current_user.foto = image_name
        current_user.cursos = atualizar_cursos(form)
        database.session.commit()
        flash(f'Perfil atualizado com sucesso', 'alert-success')
        return redirect(url_for('perfil'))
    elif request.method == 'GET':
        form.email.data = current_user.email
        form.username.data = current_user.username

    foto_perfil = url_for('static', filename=f'foto_perfil/{current_user.foto}')
    return render_template('perfil_editar.html', form=form, foto_perfil=foto_perfil)


@app.route('/post/criar', methods=['GET', 'POST'])
@login_required
def criar_post():
    form = FormCriarPost()
    if form.validate_on_submit():
        post = Post(title=form.title.data, message=form.message.data, author=current_user)
        database.session.add(post)
        database.session.commit()
        flash("Post criado com sucesso!", "alert-success")
        return redirect(url_for('index'))
    return render_template('post_criar.html', form=form)


@app.route('/post/<post_id>', methods=['GET', 'POST'])
@login_required
def post_view(post_id):
    post = Post.query.get(post_id)
    if current_user == post.author:
        form = FormCriarPost()
        if request.method == 'GET':
            form.title.data = post.title
            form.message.data = post.message
        elif form.validate_on_submit():
            post.title = form.title.data
            post.message = form.message.data
            database.session.commit()
            flash('Post atualizado com sucesso!', 'alert-success')
            return redirect(url_for('index'))
    else:
        form = None
    return render_template('post.html', post=post, form=form)


@app.route('/post/<post_id>/delete', methods=['GET', 'POST'])
@login_required
def post_delete(post_id):
    post = Post.query.get(post_id)
    if current_user == post.author:
        database.session.delete(post)
        database.session.commit()
        flash('Post excluído com sucesso!', 'alert-success')
        return redirect(url_for('index'))
    else:
        abort(403)
