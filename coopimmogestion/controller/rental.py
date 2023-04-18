from flask import render_template, request, escape, redirect, url_for, flash, Blueprint
from ..decorators.login_required import login_required
from ..models.Rental import Rental
from ..models.Tenant import Tenant
from ..models.Apartment import Apartment


rental = Blueprint('rental', __name__, template_folder='templates')


@rental.get('/locations')
@login_required
def rental_read_all():
    page_title = 'CoopImmoGestion-Locations'
    rentals = Rental.read()
    tenants = Tenant.read()
    apartments = Apartment.read()
    # If connection database error
    if not isinstance(rentals, list):
        flash("Une erreur est survenue, veuillez actualiser la page", "error")

    return render_template('rental.html', page_title=page_title,
                           rentals=rentals, tenants=tenants, apartments=apartments)


@rental.post('/locations/creer')
@login_required
def rental_create():
    # Escape form inputs values
    user_input = {name: escape(value) for name, value in request.form.items()}
    # Create Apartment and associate Address
    rental: Rental = Rental.create(user_input)

    if rental:
        flash("Succès de la création de la location", "success")
    else:
        flash("Erreur lors de la création de la location", "error")

    return redirect(url_for('rental.rental_read_all'))
