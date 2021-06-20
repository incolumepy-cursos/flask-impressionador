#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = '@britodfbr'

from datetime import datetime
from jedi import database, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(id_user):
    return Usuario.query.get(int(id_user))


class Usuario(database.Model, UserMixin):
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String, nullable=False)
    email = database.Column(database.String, nullable=False, unique=True)
    password = database.Column(database.String, nullable=False)
    foto = database.Column(database.String, default='user_color.svg')
    posts = database.relationship('Post', backref='author', lazy=True)
    cursos = database.Column(database.String, nullable=False, default='[]')


class Post(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    title = database.Column(database.String, nullable=False)
    message = database.Column(database.Text, nullable=False)
    criated = database.Column(database.DateTime, nullable=False, default=datetime.utcnow)
    id_usuario = database.Column(database.Integer, database.ForeignKey('usuario.id'), nullable=False)
