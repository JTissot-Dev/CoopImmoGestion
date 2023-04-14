from flask import render_template, request, escape, redirect, url_for, flash, Blueprint
from ..decorators.login_required import login_required
from ..models.Apartment import Apartment
from ..models.Address import Address


apartment = Blueprint('apartment', __name__, template_folder='templates')


@apartment.get('/appartements')
@login_required
def apartment_read_all():
    page_title = 'CoopImmoGestion-appartements'
    apartments = Apartment.read()
    # If connection database error
    if not isinstance(apartments, list):
        flash("Une erreur est survenue, veuillez actualiser la page", "error")

    return render_template('apartment.html', page_title=page_title,
                           apartments=apartments)


@apartment.post('/appartements/creer')
@login_required
def apartment_create():
    # Escape form inputs values
    user_input = {name: escape(value) for name, value in request.form.items()}
    # Create Apartment and associate Address
    apartment_address: Address = Address.create(user_input)
    apartment: Apartment = Apartment.create(user_input, apartment_address)

    if apartment:
        flash("Succès de la création de l'appartement", "success")
    else:
        flash("Erreur lors de la création de l'appartement", "error")

    return redirect(url_for('apartment.apartment_read_all'))
