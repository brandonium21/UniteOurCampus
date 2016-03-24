from app import app
from flask import redirect, render_template, render_template_string, request, url_for, json

@app.route('/')
def root():
    return app.send_static_file('index.html')

@app.route('/register', methods=['GET', 'POST'])
def reg():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        print name
        print email
    return render_template('register.html')
