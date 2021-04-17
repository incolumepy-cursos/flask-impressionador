#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = '@britodfbr'
from flask import Flask, render_template, url_for, request, flash, redirect
from forms import FormCriarConta, FormLogin
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = 'b3612c4882b0dbe427aef77d018686bcf366f4886c6eabee'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///jedi_db.sqlite'
lista_usuarios = ['Lira', 'Brito', 'Ana', 'Ada', 'Eliana', 'Leni', 'Ricardo']


database = SQLAlchemy(app)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form_login = FormLogin()
    form_criar_conta = FormCriarConta()
    if form_login.validate_on_submit() and 'submit_login' in request.form:
        flash(f'Login realizado com sucesso: {form_login.email.data}!', 'alert-success')
        return redirect(url_for('home'))
    if form_criar_conta.validate_on_submit() and 'submit_criar_conta' in request.form:
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


if __name__ == '__main__':
    app.run(debug=True)
