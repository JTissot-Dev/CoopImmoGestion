from flask import render_template, request, escape, redirect, url_for
from flask.views import View
from ..models.AppUser import AppUser


class LoginView(View):
    methods = ['GET', 'POST']

    def dispatch_request(self):
        page_title = 'CoopImmoGestion-connexion'
        if request.method == 'POST':
            # Escape form input value
            user_email = escape(request.form['email'])
            user_password = escape(request.form['password'])
            # Validate email and password user
            if AppUser.login(user_email, user_password):
                return redirect(url_for('index_view'))
            return render_template('login.html',
                                   page_title=page_title,
                                   error_log='Adresse e-mail ou mot de passe invalide')
        return render_template('login.html',
                               page_title=page_title,
                               error_log='')


