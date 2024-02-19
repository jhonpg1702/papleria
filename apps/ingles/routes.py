# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from apps.ingles import blueprint 
from flask import render_template, request,session,redirect,url_for
from flask_login import login_required
from jinja2 import TemplateNotFound


@blueprint.route('/ingles')

def ingles():

    return render_template('ingles/index.html', segment='index')

