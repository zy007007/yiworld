# -*- coding:utf-8 -*-
from flask import redirect, url_for
from forms.login import LoginForm, RegisterForm

from flask import Blueprint
from helpers.override import tmpl
from models.user import UserModel
from config.ext import db
from flask_login import login_user

__all__ = ['bp']

bp = Blueprint('login', __name__, url_prefix='/')


@bp.route('login', methods=['GET', 'POST'])
def index():
    form = LoginForm()
    if form.validate_on_submit():
        user = UserModel.query.filter_by(name=form.name.data).first()
        if user:
            login_user(user, form.remember_me.data)
            return redirect(url_for('main.home'))
    return tmpl(form=form)


@bp.route('register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = UserModel(name=form.name.data,
                         password=form.password.data,
                         mobile=form.mobile.data
                         )
        db.session.add(user)
        return redirect(url_for('login.index'))
    return tmpl(form=form)


