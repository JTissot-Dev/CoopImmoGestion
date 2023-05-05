from flask import render_template, request, escape, redirect, url_for, flash, Blueprint, make_response
from ..decorators.login_required import login_required
from ..decorators.admin_required import admin_required
from ..models.Rent import Rent
from ..models.AgencyFee import AgencyFee
from ..models.SecurityDeposit import SecurityDeposit
from ..models.Rental import Rental
from ..smtp.smtp import mail
from flask_mail import Message
from datetime import datetime as dt
import pandas as pd
import io


finance = Blueprint('finance', __name__, template_folder='templates')


@finance.get('/finances')
@login_required
def finance_read_all():
    page_title = 'CoopImmoGestion-Finances'
    rents = Rent.read(None)
    security_deposits = SecurityDeposit.read()
    rentals = Rental.read()
    agency_fee = AgencyFee.read()

    # If connection database error
    if not isinstance(rents, list) or not isinstance(security_deposits, list):
        payments = None
        flash("Une erreur est survenue, veuillez actualiser la page", "error")
    else:
        payments = rents + security_deposits

    return render_template('finance.html', page_title=page_title,
                           payments=payments, rentals=rentals, agency_fee=agency_fee)


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


@finance.post('/finances/modifier/<int:payment_id>')
@login_required
def finance_update(payment_id):
    # Escape form inputs values
    user_input = {name: escape(value) for name, value in request.form.items()}
    # Create Rent or SecurityDeposit
    if user_input['type_payment'] == 'Loyer':
        # Decrease rental balance with current rent amount
        payment: Rent = Rent.read(payment_id)
        Rental.delete_payment_balance(payment.rental_id, payment)
        # Update rent values
        payment: Rent = Rent.update(payment_id, user_input)
        # Increase rental balance with update rent amount
        Rental.add_payment_balance(payment.rental_id, payment)
    elif user_input['type_payment'] == 'Dépôt de garantie':
        payment: SecurityDeposit = SecurityDeposit.update(payment_id, user_input)

    if payment:
        flash("Succès de la mise à jour du paiement", "success")
    else:
        flash("Erreur lors de la mise à jour du paiement", "error")

    return redirect(url_for('finance.finance_read_all'))


# Delete rent
@finance.get('/finances/loyer/supprimer/<int:payment_id>')
@login_required
def rent_delete(payment_id):
    # Delete Rent concerned by payment_id
    rent = Rent.delete(payment_id)
    if rent:
        Rental.delete_payment_balance(rent.rental_id, rent)
        flash("Succès de la suppression du paiement", "success")
    else:
        flash("Erreur lors de la suppression du paiement", "error")

    return redirect(url_for('finance.finance_read_all'))


# Delete security deposit
@finance.get('/finances/depot-garantie/supprimer/<int:payment_id>')
@login_required
def security_deposit_delete(payment_id):
    # Delete Security deposit concerned by payment_id
    if SecurityDeposit.delete(payment_id):
        flash("Succès de la suppression du paiement", "success")
    else:
        flash("Erreur lors de la suppression du paiement", "error")

    return redirect(url_for('finance.finance_read_all'))


# Send email with rent receipt concerned by rental
@finance.post('/finances/quittance-loyer')
@login_required
def send_rent_receipt():
    # Escape form inputs values
    user_input = {name: escape(value) for name, value in request.form.items()}

    rental = Rental.read(user_input['rental_id'])
    start_date = Rental.convert_date(user_input['start_date'])
    end_date = Rental.convert_date(user_input['end_date'])

    msg = Message(f'Quittance de loyer {rental.apartment.reference}', sender='coopimmogestion@gmail.com',
                  recipients=[rental.tenant.email])
    msg.html = render_template('rent_receipt.html', rental=rental, start_date=start_date,
                               end_date=end_date, text_start_date=user_input['start_date'],
                               text_end_date=user_input['end_date'])

    # Check if rental payments are conformed for the period before sending email
    if rental.check_rental_payment(start_date, end_date):
        try:
            mail.send(msg)
            flash("Quittance de loyer envoyée avec succès", "success")
        except Exception:
            flash("Erreur lors de l'envoie de la quittance de loyer", "error")
    else:
        flash("Le locataire n'est pas en règle des règlements sur cette periode", "error")

    return redirect(url_for('finance.finance_read_all'))


# Access account balance page
@finance.post('/finances/bilan-des-comptes')
@login_required
def account_balances():
    page_title = 'CoopImmoGestion-Bilan-des-comptes'

    # Escape form inputs values
    rental_id = escape(request.form['rental_id'])
    rental = Rental.read(rental_id)

    # Get detail from rental payments
    rents_detail = rental.extract_balance_account()
    total_amount = rents_detail['total_amount']
    payment_number = rents_detail['payment_number']
    rents_excluding_charges_amount = rents_detail['rents_excluding_charges_amount']
    charges_amount = rents_detail['charges_amount']
    agency_fee_amount = rents_detail['agency_fee_amount']

    return render_template('account_balance.html',
                           page_title=page_title,
                           rental=rental,
                           payment_number=payment_number,
                           total_amount=total_amount,
                           rents_excluding_charges_amount=rents_excluding_charges_amount,
                           charges_amount=charges_amount,
                           agency_fee_amount=agency_fee_amount)


# Export account balance data in xlsx
@finance.post('/finances/bilan-des-comptes/export/<int:rental_id>')
@login_required
def account_balances_export(rental_id):
    rental = Rental.read(rental_id)

    # Get detail from rental payments
    rents_detail = rental.extract_balance_account()

    # Define data structure for DataFrame
    series = pd.Series(rents_detail,
                       name=f'Bilan_des_comptes: {rental.tenant.full_name} {rental.apartment.reference}')
    series.index = [
        'Nombre de loyers perçus',
        'Loyers hors charges',
        'Charges',
        'Total perçu',
        'Frais d\'agence'
    ]

    export_file = pd.DataFrame(data=series)

    # Store Excel file in RAM
    buffer = io.BytesIO()

    # write data in Excel file
    with pd.ExcelWriter(buffer) as writer:
        export_file.to_excel(writer, sheet_name=f'{rental.text_start_date} au {rental.text_end_date}')

    # Define response
    response = make_response(buffer.getvalue())
    response.headers['Content-Disposition'] = \
        f'attachment; filename=Bilan_des_comptes_{dt.strftime(dt.now(), "%Y-%m-%d")}.xlsx'
    response.headers['Content-Type'] = 'application/vnd.ms-excel'

    return response


@finance.post('/finances/frais-agence/modifier')
@login_required
@admin_required
def agency_fee_update():
    # Escape form input value
    rate = escape(request.form['rate'])

    agency_fee: AgencyFee = AgencyFee.update(rate)

    if agency_fee:
        flash("Succès de la mise à jour des frais d'agence", "success")
    else:
        flash("Erreur lors de la mise à jour des frais d'agence", "error")

    return redirect(url_for('finance.finance_read_all'))

