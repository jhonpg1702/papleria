# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from apps.home import blueprint 
from flask import render_template, request,session,redirect,url_for
from flask_login import login_required
from jinja2 import TemplateNotFound
import plotly.io as pio
import pandas as pd

from .data import create_dataframe

@blueprint.route('/dashapp')
def dashapp():
    df = create_dataframe()
    plot_div = pio.to_html(
        {
            "data": [
                {
                    "x": df["complaint_type"],
                    "text": df["complaint_type"],
                    "customdata": df["key"],
                    "name": "311 Calls by region.",
                    "type": "histogram",
                }
            ],
            "layout": {
                
                "height": 700,
                "margin": {
                    "pad": 50
                },
            },
        },
        full_html=False
    )
    return render_template('dashapp/dashapp.html', plot_div=plot_div, table=df.to_dict(orient='records'))


