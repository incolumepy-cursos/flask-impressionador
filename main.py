#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = '@britodfbr'
from flask import Flask, render_template, url_for
app = Flask(__name__)
lista_usuarios = ['Lira', 'Brito', 'Ana', 'Ada', 'Eliana', 'Leni', 'Ricardo']


@app.route('/login')
def login():
    return render_template('login.html')


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
