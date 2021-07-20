from flask_app import app
from flask import render_template, request, redirect, session, flash
from flask_app.models.email import Email

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/success')
def success():
    return render_template('success.html')