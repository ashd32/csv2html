from flask import Blueprint, render_template, redirect, url_for, flash
from .database import db
import plotly.graph_objects as go

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def index():

    fig = go.Figure(data=go.Bar(y=[2, 3, 1]))
    fig.show()

    return render_template('index.html')

@views.route('/about/')
def about():
    return render_template('about.html')

