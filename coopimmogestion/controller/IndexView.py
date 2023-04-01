from flask import render_template, session
from flask.views import View
from ..decorators.login_required import login_required


class IndexView(View):
    methods = ['GET']

    @login_required
    def dispatch_request(self):
        page_title = 'CoopImmoGestion-acceuil'
        user_first_name = session['userfirstname']
        return render_template('index.html', page_title=page_title,
                               user_first_name=user_first_name)
