# -*- coding:utf-8 -*-
from flask import redirect, url_for, Blueprint
from helpers.override import tmpl
from flask_login import login_required, current_user, logout_user
from models.backend import DailycostDoc
from forms.backend import DailycostForm

import sys
reload(sys)
sys.setdefaultencoding("utf-8")


__all__ = ['bp']

bp = Blueprint('backend', __name__, url_prefix='/backend')


@bp.route("/main")
@login_required
def backend():
    user = current_user.name
    return tmpl(user=user)


@bp.route("/daily")
@login_required
def daily_cost():
    user = current_user.name
    dailycost = DailycostDoc.objects().order_by('-date').all()
    return tmpl(user=user, dailycost=dailycost)


@bp.route("/daily/cost", methods=['GET', 'POST'])
@login_required
def daily_cost_add():
    form = DailycostForm()
    if form.validate_on_submit():
        cost = DailycostDoc(type=form.type.data,
                            money=form.money.data)
        cost.save()
        return redirect(url_for('backend.daily_cost'))
    return tmpl(form=form)