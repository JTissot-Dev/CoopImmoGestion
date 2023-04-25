from flask import render_template, request, escape, redirect, url_for, flash, Blueprint
from ..decorators.login_required import login_required
from ..models.Rent import Rent
from ..models.AgencyFee import AgencyFee
from ..models.SecurityDeposit import SecurityDeposit
from ..models.Rental import Rental


finance = Blueprint('finance', __name__, template_folder='templates')


@finance.get('/finances')
@login_required
def finance_read_all():
    page_title = 'CoopImmoGestion-Finances'
    rents = Rent.read(None)
    security_deposits = SecurityDeposit.read()
    rentals = Rental.read()

    # If connection database error
    if not isinstance(rents, list) or not isinstance(security_deposits, list):
        payments = None
        flash("Une erreur est survenue, veuillez actualiser la page", "error")
    else:
        payments = rents + security_deposits

    return render_template('finance.html', page_title=page_title,
                           payments=payments, rentals=rentals)


@finance.post('/finances/creer')
@login_required
def finance_create():
    # Escape form inputs values
    user_input = {name: escape(value) for name, value in request.form.items()}
    # Create Rent or SecurityDeposit
    if user_input['type_payment'] == 'Loyer':
        payment: Rent = Rent.create(user_input, None)
    elif user_input['type_payment'] == 'Dépôt de garantie':
        payment: SecurityDeposit = SecurityDeposit.create(user_input, None)

    if payment:
        if isinstance(payment, Rent):
            Rental.add_payment_balance(user_input['rental_id'], payment)
        flash("Succès de la création du paiement", "success")
    else:
        flash("Erreur lors de la création du paiement", "error")

    return redirect(url_for('finance.finance_read_all'))
