from flask import render_template
from flask.views import View


class LoginView(View):
    methods = ['GET']

    def dispatch_request(self):
        page_title = 'CoopImmoGestion-connexion'
        return render_template('login.html', page_title=page_title)

