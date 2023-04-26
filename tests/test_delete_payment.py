from coopimmogestion.db.db import db
from datetime import datetime as dt
from coopimmogestion.models.Apartment import Apartment
from coopimmogestion.models.Tenant import Tenant
from coopimmogestion.models.Rental import Rental
from coopimmogestion.models.Address import Address
from coopimmogestion.models.Rent import Rent
from coopimmogestion.models.SecurityDeposit import SecurityDeposit


class TestDeletePayment:
    # Test delete Rent
    def test_access_delete_rent(self, client, app):
        with client.session_transaction() as session:
            session["username"] = "test@test.fr"
            session["role"] = "admin"

        TestDeletePayment.create_test_entity(app)

        response = client.get("/finances/loyer/supprimer/1", follow_redirects=True)
        assert response.status_code == 200

    def test_delete_rent(self, client, app):
        with client.session_transaction() as session:
            session["username"] = "test@test.fr"
            session["role"] = "admin"

        TestDeletePayment.create_test_entity(app)

        client.get("/finances/loyer/supprimer/1", follow_redirects=True)

        with app.app_context():
            try:
                rent_test = Rent.query.filter_by(payment_id=1).first()
            except Exception:
                rent_test = None
        assert rent_test is None

    def test_delete_rent_redirect(self, client, app):
        with client.session_transaction() as session:
            session["username"] = "test@test.fr"
            session["role"] = "admin"

        TestDeletePayment.create_test_entity(app)

        response = client.get("/finances/loyer/supprimer/1", follow_redirects=True)

        assert '<title>CoopImmoGestion-Finances</title>' in response.data.decode('utf-8')

    # Test delete Security deposit
    def test_access_delete_security_deposit(self, client, app):
        with client.session_transaction() as session:
            session["username"] = "test@test.fr"
            session["role"] = "admin"

        TestDeletePayment.create_test_entity(app)

        response = client.get("/finances/depot-garantie/supprimer/1", follow_redirects=True)
        assert response.status_code == 200

    def test_delete_security_deposit(self, client, app):
        with client.session_transaction() as session:
            session["username"] = "test@test.fr"
            session["role"] = "admin"

        TestDeletePayment.create_test_entity(app)

        client.get("/finances/depot-garantie/supprimer/1", follow_redirects=True)

        with app.app_context():
            try:
                security_deposit_test = SecurityDeposit.query.filter_by(payment_id=1).first()
            except Exception:
                security_deposit_test = None
        assert security_deposit_test is None

    def test_delete_security_deposit_redirect(self, client, app):
        with client.session_transaction() as session:
            session["username"] = "test@test.fr"
            session["role"] = "admin"

        TestDeletePayment.create_test_entity(app)

        response = client.get("/finances/depot-garantie/supprimer/1", follow_redirects=True)
        assert '<title>CoopImmoGestion-Finances</title>' in response.data.decode('utf-8')

    @staticmethod
    def create_test_entity(app):
        with app.app_context():
            address_test: Address = Address(None, 'Test', 1, '', '00000', 'Test')
            db.session.add(address_test)
            db.session.commit()

            apartment_test: Apartment = Apartment(None, 'Apartement-test', 150, 5, address_test,
                                                  2, True, 400, 100, 700)
            tenant_test: Tenant = Tenant(None, 'Test', 'Test', dt.now(), '0000000102', 'test@test.fr',
                                         address_test, 'Test', 30000)
            db.session.add(apartment_test)
            db.session.add(tenant_test)
            db.session.commit()

            rental_test: Rental = Rental(None, dt.strptime('2023-01-01', '%Y-%m-%d'),
                                         dt.strptime('2023-04-01', '%Y-%m-%d'), 1, 1)
            db.session.add(rental_test)
            db.session.commit()

            rent_test = Rent(None, 500, dt.now(), 'Locataire', 1, 1)
            db.session.add(rent_test)
            db.session.commit()

            security_deposit_test = SecurityDeposit(None, 600, dt.now(), 1)
            db.session.add(security_deposit_test)
            db.session.commit()
