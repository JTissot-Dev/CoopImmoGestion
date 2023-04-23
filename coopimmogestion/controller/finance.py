from flask import render_template, request, escape, redirect, url_for, flash, Blueprint
from ..decorators.login_required import login_required
from ..models.Rent import Rent
from ..models.AgencyFee import AgencyFee
from ..models.SecurityDeposit import SecurityDeposit


finance = Blueprint('finance', __name__, template_folder='templates')


@finance.get('/finances')
@login_required
def finance_read_all():
    page_title = 'CoopImmoGestion-Finances'
    rents = Rent.read()
    security_deposits = SecurityDeposit.read()

    # If connection database error
    if not isinstance(rents, list) or not isinstance(security_deposits, list):
        payments = None
        flash("Une erreur est survenue, veuillez actualiser la page", "error")
    else:
        payments = rents + security_deposits

    return render_template('finance.html', page_title=page_title,
                           payments=payments)
