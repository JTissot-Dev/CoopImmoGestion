from flask import render_template, request, escape, redirect, url_for, flash, Blueprint
from ..decorators.login_required import login_required
from ..models.Rental import Rental
from ..models.Tenant import Tenant
from ..models.Apartment import Apartment
from ..models.Address import Address
from ..models.Inventory import Inventory


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


@rental.post('/locations/modifier/<int:rental_id>')
@login_required
def rental_update(rental_id):
    # Escape form inputs values
    user_input = {name: escape(value) for name, value in request.form.items()}
    # Update Rental
    rental: Rental = Rental.update(rental_id, user_input)

    if rental:
        flash("Succès de la mise à jour de la location", "success")
    else:
        flash("Erreur lors de la mise à jour de la location", "error")

    return redirect(url_for('rental.rental_read_all'))


# Update rental tenant
@rental.post('/locations/locataire/modifier/<int:person_id>')
@login_required
def rental_tenant_update(person_id):
    # Escape form inputs values
    user_input = {name: escape(value) for name, value in request.form.items()}
    # Update Apartment
    tenant_address: Address = Address.create(user_input)
    tenant: Tenant = Tenant.update(person_id, user_input, tenant_address)

    if tenant:
        flash("Succès de la mise à jour du locataire", "success")
    else:
        flash("Erreur lors de la mise à jour du locataire", "error")

    return redirect(url_for('rental.rental_read_all'))


# Update rental apartment
@rental.post('/locations/appartement/modifier/<int:property_id>')
@login_required
def rental_apartment_update(property_id):
    # Escape form inputs values
    user_input = {name: escape(value) for name, value in request.form.items()}
    # Update Apartment
    apartment_address: Address = Address.create(user_input)
    apartment: Apartment = Apartment.update(property_id, user_input, apartment_address)

    if apartment:
        flash("Succès de la mise à jour de l'appartement", "success")
    else:
        flash("Erreur lors de la mise à jour de l'appartement", "error")

    return redirect(url_for('rental.rental_read_all'))


@rental.post('/locations/etat-des-lieux/creer/<int:rental_id>')
@login_required
def rental_inventory_create(rental_id):
    # Escape form inputs values
    user_input = {name: escape(value) for name, value in request.form.items()}
    # Create Apartment and associate Address
    inventory: Inventory = Inventory.create(user_input, rental_id)

    if inventory:
        flash("Succès de la création de l'état des lieux", "success")
    else:
        flash("Erreur lors de la création de l'état des lieux", "error")

    return redirect(url_for('rental.rental_read_all'))


@rental.get('/locations/supprimer/<int:rental_id>')
@login_required
def rental_delete(rental_id):
    # Delete Rental concerned by rental_id
    if Rental.delete(rental_id):
        flash("Succès de la suppression de la location", "success")
    else:
        flash("Erreur lors de la suppression de la location", "error")

    return redirect(url_for('rental.rental_read_all'))