# -*- coding:utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import BooleanField
from wtforms import PasswordField
from wtforms import StringField
from wtforms import SubmitField
from wtforms.validators import DataRequired

__all__ = ['LoginForm', 'RegisterForm']


class LoginForm(FlaskForm):
    name = StringField(u'用户名', validators=[DataRequired()])
    password = PasswordField(u'密码', validators=[DataRequired()])
    remember_me = BooleanField(u'下次自动登录')
    submit = SubmitField(u'登录')


class RegisterForm(FlaskForm):
    name = StringField(u'姓名')
    password = StringField(u'密码')
    mobile = StringField(u'手机号')
    submit = SubmitField(u'注册')