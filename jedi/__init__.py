#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = '@britodfbr'

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = 'b3612c4882b0dbe427aef77d018686bcf366f4886c6eabee'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///jedi_db.sqlite'

database = SQLAlchemy(app)

from jedi import routes
