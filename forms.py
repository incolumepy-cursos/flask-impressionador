#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = '@britodfbr'
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class FormCriarConta(FlaskForm):
    username = StringField('Nome de Usuário', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    email_confirmation = StringField('Email confimação', validators=[DataRequired(), EqualTo('email')])
    password = PasswordField('Senha', validators=[DataRequired(), Length(6, 20)])
    password_confirmation = PasswordField('Senha confirmação', validators=[DataRequired(), EqualTo("password")])
    submit_criar_conta = SubmitField('Criar Conta')


class FormLogin(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('senha', validators=[DataRequired(), Length(6, 20)])
    lembrar_dados = BooleanField('Lembrar dados acesso')
    submit_login = SubmitField('Login')
