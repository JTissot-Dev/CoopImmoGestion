from flask import redirect, url_for, Blueprint
from ..decorators.login_required import login_required
from ..models.AppUser import AppUser

logout = Blueprint('logout', __name__, template_folder='templates')


@logout.get('/deconnexion')
@login_required
def logout_get():
    AppUser.logout()
    return redirect(url_for('login.login_get'))




