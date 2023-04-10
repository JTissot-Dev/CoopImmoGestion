from flask import render_template, request, escape, redirect, url_for, flash, Blueprint
from ..decorators.login_required import login_required
from ..decorators.admin_required import admin_required
from ..models.Address import Address
from ..models.AppUser import AppUser


account = Blueprint('account', __name__, template_folder='templates')


@account.get('/comptes')
@login_required
@admin_required
def account_read_all():
    page_title = 'CoopImmoGestion-comptes'
    users: list = AppUser.read()
    if not users:
        flash("Erreur lors du chargement des comptes utilisateurs")

    return render_template('account.html', page_title=page_title,
                           users=users)


@account.post('/comptes/creer')
@login_required
@admin_required
def account_create():
    # Escape form inputs values
    user_input = {name: escape(value) for name, value in request.form.items()}
    # Create User and associate address
    app_user_address: Address = Address.create(user_input)
    user: AppUser = AppUser.create(user_input, app_user_address)

    if user:
        flash("Succès de la création du compte utilisateur")
    else:
        flash("Erreur lors de la création du compte utilisateur")

    return redirect(url_for('account.account_read_all'))




