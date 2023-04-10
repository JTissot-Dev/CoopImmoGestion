from flask import render_template, session, Blueprint
from ..decorators.login_required import login_required

index = Blueprint('index', __name__, template_folder='templates')


@index.get('/')
@login_required
def index_get():
    page_title = 'CoopImmoGestion-acceuil'
    user_first_name = session['userfirstname']
    return render_template('index.html', page_title=page_title,
                           user_first_name=user_first_name)


