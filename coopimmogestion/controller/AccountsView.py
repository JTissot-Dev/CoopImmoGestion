from flask import render_template, request, escape, redirect, url_for, flash
from flask.views import View
from ..decorators.login_required import login_required
from ..decorators.admin_required import admin_required
from ..crypt.crypt import bcrypt
from ..db.db import db
from datetime import datetime as dt
from ..models.Address import Address
from ..models.AppUser import AppUser


class AccountView(View):
    methods = ['GET', 'POST']

    @login_required
    @admin_required
    def dispatch_request(self):
        if request.method == 'POST':
            # Escape form inputs values
            user_entry = {name: escape(value) for name, value in request.form.items()}

            user_address = Address(None, user_entry['street_name'], user_entry['street_number'],
                                   user_entry['additionnal_address'], user_entry['zip_code'], user_entry['city'])

            # Put input birthday in datetime format
            user_birthday = dt.strptime(user_entry['birthday'], "%Y-%m-%d")
            # Hashing password
            user_password = bcrypt.generate_password_hash(user_entry['password'])

            try:
                exist_address = Address.query.filter_by(street_name=user_address.street_name,
                                                        street_number=user_address.street_number,
                                                        additional_address=user_address.additional_address,
                                                        zip_code=user_address.zip_code, city=user_address.city).first()
                if not exist_address:
                    db.session.add(user_address)
                    db.session.commit()
                else:
                    user_address = exist_address
            except Exception:
                flash("Erreur lors de la création de l'adresse utilisateur")
                return redirect(url_for('account_view'))

            user = AppUser(None, user_entry['first_name'], user_entry['last_name'], user_birthday,
                           user_entry['phone_number'], user_entry['email'], user_address, user_entry['role'].lower(),
                           user_password)

            try:
                db.session.add(user)
                db.session.commit()
            except Exception:
                flash("Erreur lors de la création de l'utilisateur")
                return redirect(url_for('account_view'))

            flash("Succès de la création du compte utilisateur")
            return redirect(url_for('account_view'))

        page_title = 'CoopImmoGestion-comptes'
        users = AppUser.query.all()
        return render_template('account.html', page_title=page_title,
                               users=users)
