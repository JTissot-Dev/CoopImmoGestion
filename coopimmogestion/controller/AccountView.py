from flask import render_template, session
from flask.views import View
from ..decorators.login_required import login_required
from ..decorators.admin_required import admin_required


class AccountView(View):
    methods = ['GET']

    @login_required
    @admin_required
    def dispatch_request(self):
        page_title = 'CoopImmoGestion-comptes'
        return render_template('account.html', page_title=page_title,
                               users='')
