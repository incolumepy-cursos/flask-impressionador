#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = '@britodfbr'

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'b3612c4882b0dbe427aef77d018686bcf366f4886c6eabee'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///jedi_db.sqlite'

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

from jedi import routes
