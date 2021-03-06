from flask_app import app
from flask import render_template, request, redirect, session, flash
from flask_app.models.email import Email

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/success')
def success():
    email = Email.get_all_emails()
    flash("Success")
    return render_template('success.html', email = email)

@app.route('/process', methods=['POST'])
def process():
    if not Email.validate_email(request.form):
        return redirect('/')
    Email.add_email(request.form)
    return redirect('/success')
