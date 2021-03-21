#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = '@britodfbr'
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class FormCriarConta(FlaskForm):
    username = StringField('Nome de Usuário', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    email_confirmation = StringField('Email confimação', validators=[DataRequired(), EqualTo('email')])
    password = PasswordField('senha', validators=[DataRequired(), Length(6, 20)])
    password_confirmation = PasswordField('confirmação de senha', validators=[DataRequired(), EqualTo("password")])
    submit_criar_conta = SubmitField('Criar Conta')


class FormLogin(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('senha', validators=[DataRequired(), Length(6, 20)])
    submit_login = SubmitField('Login')
