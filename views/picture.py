# -*- coding:utf-8 -*-
from flask import redirect, url_for, Blueprint
from helpers.override import tmpl
from flask_login import login_required, current_user, logout_user
from models.user import UserModel

import sys
reload(sys)
sys.setdefaultencoding("utf-8")


__all__ = ['bp']

bp = Blueprint('picture', __name__, url_prefix='/picture')


@bp.route("/list")
@login_required
def picture_list():
    user = current_user.name
    return tmpl(user=user)



