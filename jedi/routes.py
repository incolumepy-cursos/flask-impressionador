#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = '@britodfbr'

from jedi import app, database
from jedi.models import Usuario
from jedi.forms import FormCriarConta, FormLogin
from flask import render_template, url_for, request, flash, redirect

lista_usuarios = ['Lira', 'Brito', 'Ana', 'Ada', 'Eliana', 'Leni', 'Ricardo']


@app.route('/login', methods=['GET', 'POST'])
def login():
    form_login = FormLogin()
    form_criar_conta = FormCriarConta()
    if form_login.validate_on_submit() and 'submit_login' in request.form:
        flash(f'Login realizado com sucesso: {form_login.email.data}!', 'alert-success')
        return redirect(url_for('home'))
    if form_criar_conta.validate_on_submit() and 'submit_criar_conta' in request.form:
        usuario = Usuario(username=form_criar_conta.username.data,
                          password=form_criar_conta.password.data,
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


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/contato')
def contato():
    return render_template('contato.html')


@app.route('/usuarios')
def usuarios():
    return render_template('usuarios.html', lista_usuarios=lista_usuarios)
