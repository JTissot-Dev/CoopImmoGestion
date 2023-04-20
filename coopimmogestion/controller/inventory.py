from flask import render_template, request, escape, redirect, url_for, flash, Blueprint
from ..decorators.login_required import login_required
from ..models.Inventory import Inventory


inventory = Blueprint('inventory', __name__, template_folder='templates')


@inventory.get('/etat-des-lieux')
@login_required
def inventory_read_all():
    page_title = 'CoopImmoGestion-Etat des lieux'
    inventories = Inventory.read()
    # If connection database error
    if not isinstance(inventories, list):
        flash("Une erreur est survenue, veuillez actualiser la page", "error")

    return render_template('inventory.html', page_title=page_title,
                           inventories=inventories)
