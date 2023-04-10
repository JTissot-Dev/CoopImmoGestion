from flask import render_template, request, escape, redirect, url_for, Blueprint
from ..models.AppUser import AppUser

login = Blueprint('login', __name__, template_folder='templates')


@login.get('/connexion')
def login_get():
    page_title = 'CoopImmoGestion-connexion'
    return render_template('login.html',
                           page_title=page_title,
                           error_log='')


@login.post('/connexion')
def login_post():
    page_title = 'CoopImmoGestion-connexion'
    # Escape form input value
    user_email = escape(request.form['email'])
    user_password = escape(request.form['password'])
    # Validate email and password user
    if AppUser.login(user_email, user_password):
        return redirect(url_for('index.index_get'))
    return render_template('login.html',
                           page_title=page_title,
                           error_log='Adresse e-mail ou mot de passe invalide')




