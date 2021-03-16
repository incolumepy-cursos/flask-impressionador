#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = '@britodfbr'
from flask import Flask
app = Flask(__name__)


@app.route('/')
@app.route('/home')
def hello_world():
    return '<h1>Hello, World</h1> <p>Hello, World!</p>'


@app.route('/contato')
def contato():
    return "Qualquer dúvida entre em contado pelo email contato@incolume.com.br"


if __name__ == '__main__':
    app.run(debug=True)
