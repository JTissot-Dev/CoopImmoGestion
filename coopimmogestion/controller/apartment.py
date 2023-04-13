from flask import render_template, request, escape, redirect, url_for, flash, Blueprint
from ..decorators.login_required import login_required
from ..decorators.admin_required import admin_required
from ..models.Apartment import Apartment


apartment = Blueprint('apartment', __name__, template_folder='templates')


@apartment.get('/appartements')
@login_required
def apartment_read_all():
    page_title = 'CoopImmoGestion-appartements'
    apartments: list = Apartment.read()
    if not apartments:
        flash("Erreur lors du chargement des appartements", "error")

    return render_template('apartment.html', page_title=page_title,
                           apartments=apartments)

