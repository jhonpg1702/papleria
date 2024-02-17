# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import Email,EqualTo, DataRequired

# login and registration


class LoginForm(FlaskForm):
    email = StringField('Email',
                         id='email_login',
                         validators=[DataRequired()])
    password = PasswordField('Password',
                             id='pwd_login',
                             validators=[DataRequired()])


class CreateAccountForm(FlaskForm):

    name = StringField("First name", validators=[DataRequired()])
    last_name = StringField("Last name", validators=[DataRequired()])

    email = StringField('Email',
                      id='email_create',
                      validators=[DataRequired(), Email()])
    
    password = PasswordField('Password',
                             id='pwd_create',
                             validators=[DataRequired()])
    confirm = PasswordField(
        "Confirm password",
        validators=[
            DataRequired(),
            EqualTo("password", message="Passwords must match."),
        ],
    )