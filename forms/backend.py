# -*- coding:utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import BooleanField
from wtforms import FloatField
from wtforms import StringField
from wtforms import SubmitField
from wtforms.validators import DataRequired

__all__ = ['DailycostForm']


class DailycostForm(FlaskForm):
    type = StringField(u'类型', validators=[DataRequired()])
    money = FloatField(u'花费', validators=[DataRequired()])
    submit = SubmitField(u'增加')