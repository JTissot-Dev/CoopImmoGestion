from flask import redirect, url_for
from flask.views import View
from ..decorators.login_required import login_required
from ..models.AppUser import AppUser


class LogoutView(View):
    methods = ['GET']

    @login_required
    def dispatch_request(self):
        AppUser.logout()
        return redirect(url_for('login_view'))
