#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = '@britodfbr'
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
@app.route('/home')
def hello_world():
    return render_template('home.html')


@app.route('/contato')
def contato():
    return render_template('contato.html')


if __name__ == '__main__':
    app.run(debug=True)
