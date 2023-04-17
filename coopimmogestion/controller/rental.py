from flask import render_template, request, escape, redirect, url_for, flash, Blueprint
from ..decorators.login_required import login_required
from ..models.Rental import Rental


rental = Blueprint('rental', __name__, template_folder='templates')


@rental.get('/locations')
@login_required
def rental_read_all():
    page_title = 'CoopImmoGestion-Locations'
    rentals = Rental.read()
    # If connection database error
    if not isinstance(rentals, list):
        flash("Une erreur est survenue, veuillez actualiser la page", "error")

    return render_template('rental.html', page_title=page_title,
                           rentals=rentals)

