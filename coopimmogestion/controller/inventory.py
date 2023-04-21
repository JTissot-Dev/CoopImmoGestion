from flask import render_template, request, escape, redirect, url_for, flash, Blueprint
from ..decorators.login_required import login_required
from ..models.Inventory import Inventory
from ..models.Rental import Rental


inventory = Blueprint('inventory', __name__, template_folder='templates')


@inventory.get('/etat-des-lieux')
@login_required
def inventory_read_all():
    page_title = 'CoopImmoGestion-Etat des lieux'
    inventories = Inventory.read()
    rentals = Rental.read()
    # If connection database error
    if not isinstance(inventories, list):
        flash("Une erreur est survenue, veuillez actualiser la page", "error")

    return render_template('inventory.html', page_title=page_title,
                           inventories=inventories, rentals=rentals)


@inventory.post('/etat-des-lieux/creer')
@login_required
def inventory_create():
    # Escape form inputs values
    user_input = {name: escape(value) for name, value in request.form.items()}
    # Create Apartment and associate Address
    inventory: Inventory = Inventory.create(user_input, None)

    if inventory:
        flash("Succès de la création de l'état des lieux", "success")
    else:
        flash("Erreur lors de la création de l'état des lieux", "error")

    return redirect(url_for('inventory.inventory_read_all'))


@inventory.post('/etat-des-lieux/modifier/<int:inventory_id>')
@login_required
def inventory_update(inventory_id):
    # Escape form inputs values
    user_input = {name: escape(value) for name, value in request.form.items()}
    # Update Rental
    inventory: Inventory = Inventory.update(inventory_id, user_input)

    if inventory:
        flash("Succès de la mise à jour de l'état des lieux", "success")
    else:
        flash("Erreur lors de la mise à jour de l'état des lieux", "error")

    return redirect(url_for('inventory.inventory_read_all'))


@inventory.get('/etat-des-lieux/supprimer/<int:inventory_id>')
@login_required
def inventory_delete(inventory_id):
    # Delete Rental concerned by rental_id
    if Inventory.delete(inventory_id):
        flash("Succès de la suppression de l'état des lieux", "success")
    else:
        flash("Erreur lors de la suppression de l'état des lieux", "error")

    return redirect(url_for('inventory.inventory_read_all'))
