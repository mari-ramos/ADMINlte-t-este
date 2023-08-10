# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, ValidationError
from wtforms.validators import DataRequired

# login and registration


class LoginForm(FlaskForm):
    username = StringField('Nome da Família',
                         id='username_login',
                         validators=[DataRequired()])
    password = PasswordField('Senha',
                             id='pwd_login',
                             validators=[DataRequired()])


class CreateAccountForm(FlaskForm):
    username = StringField('Nome da Família',
                         id='username_create',
                         validators=[DataRequired()])
    phone = StringField('Número de Telefone', validators=[DataRequired()])
    password = PasswordField('Senha', validators=[DataRequired()])



    
# def validate_phone(form, field):
#        if len(field.data) > 11:
#           raise ValidationError('Número de telefone inválido')
#       try:
#           input_number = phonenumbers.parse(field.data)
#           if not (phonenumbers.is_valid_number(input_number)):
#               raise ValidationError('Número de telefone inválido')
#       except:
#           input_number = phonenumbers.parse("+1"+field.data)
#           if not (phonenumbers.is_valid_number(input_number)):
#               raise ValidationError('Número de telefone inválido')
#   password = PasswordField('Password',

#                             id='pwd_create',
 #                            validators=[DataRequired()])


