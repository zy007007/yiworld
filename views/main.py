# -*- coding:utf-8 -*-
from flask import redirect, url_for, Blueprint
from helpers.override import tmpl
from flask_login import login_required, current_user, logout_user
from models.user import UserModel

import sys
reload(sys)
sys.setdefaultencoding("utf-8")


__all__ = ['bp']

bp = Blueprint('main', __name__, url_prefix='/main')


@bp.route("/home")
@login_required
def home():
    user = current_user.name
    return tmpl(user=user)


@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login.index'))
