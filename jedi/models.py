#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = '@britodfbr'

from datetime import datetime
from jedi import database


class Usuario(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String, nullable=False)
    email = database.Column(database.String, nullable=False, unique=True)
    password = database.Column(database.String, nullable=False)
    foto = database.Column(database.String, default='user_color.svg')
    posts = database.relationship('Post', backref='author', lazy=True)
    cursos = database.Column(database.String, nullable=False, default='Não Informado')


class Post(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    title = database.Column(database.String, nullable=False)
    message = database.Column(database.Text, nullable=False)
    criated = database.Column(database.DateTime, nullable=False, default=datetime.utcnow)
    id_usuario = database.Column(database.Integer, database.ForeignKey('usuario.id'), nullable=False)
