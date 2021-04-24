#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = '@britodfbr'
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from .models import Usuario
from flask_login import current_user


class FormCriarConta(FlaskForm):
    username = StringField('Nome de Usuário', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    email_confirmation = StringField('Email confimação', validators=[DataRequired(), EqualTo('email')])
    password = PasswordField('Senha', validators=[DataRequired(), Length(6, 20)])
    password_confirmation = PasswordField('Senha confirmação', validators=[DataRequired(), EqualTo("password")])
    submit_criar_conta = SubmitField('Criar Conta')

    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if usuario:
            raise ValidationError('Email já cadastrado. Cadastre-se com outro ou faça login para continuar')


class FormLogin(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('senha', validators=[DataRequired(), Length(6, 20)])
    lembrar_dados = BooleanField('Lembrar dados acesso')
    submit_login = SubmitField('Login')


class FormEditarPerfil(FlaskForm):
    username = StringField('Nome de Usuário', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    foto_perfil = FileField('Foto Perfil', validators=[FileAllowed(['png', 'jpg'])])

    curso_python_basico = BooleanField('Python Básico')
    curso_python_avancado = BooleanField('Python Avançado')
    curso_web_flask = BooleanField('Flask')
    curso_web_django = BooleanField('Django')
    curso_pandas = BooleanField('Pandas')
    curso_mineracao_dados = BooleanField('Mineração de Dados')
    curso_kv = BooleanField('Kivy')
    curso_gui_tkinter = BooleanField('TKInter')
    curso_gui_pygui = BooleanField('PyGUI')
    curso_automacao_python = BooleanField('Automação com Python')

    submit_editar_perfil = SubmitField('Atualizar')

    def validate_email(self, email):
        if current_user.email != email.data:
            usuario = Usuario.query.filter_by(email=email.data).first()
            if usuario:
                raise ValidationError(f'Email {email.data} '
                                      f'já cadastrado. Cadastre-se com outro ou faça login para continuar')
