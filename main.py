#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = '@britodfbr'
from flask import Flask, render_template, url_for
from forms import FormCriarConta, FormLogin

app = Flask(__name__)
app.config['SECRET_KEY'] = 'b3612c4882b0dbe427aef77d018686bcf366f4886c6eabee'
lista_usuarios = ['Lira', 'Brito', 'Ana', 'Ada', 'Eliana', 'Leni', 'Ricardo']


@app.route('/login')
def login():
    form_login = FormLogin()
    form_criar_conta = FormCriarConta()
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
