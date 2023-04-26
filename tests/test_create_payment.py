from coopimmogestion.db.db import db
from datetime import datetime as dt
from coopimmogestion.models.Apartment import Apartment
from coopimmogestion.models.Tenant import Tenant
from coopimmogestion.models.Rental import Rental
from coopimmogestion.models.Address import Address
from coopimmogestion.models.Rent import Rent
from coopimmogestion.models.SecurityDeposit import SecurityDeposit


class TestCreatePayment:
    # Test create payments from payment controller
    # Rent
    def test_send_data_rent(self, client, app):
        with client.session_transaction() as session:
            session["username"] = "test@test.fr"
            session["role"] = "admin"

        TestCreatePayment.create_test_entity(app)

        response = client.post("/finances/creer", data={
            "amount": 500,
            "payment_date": "2023-05-08",
            "observation": "test",
            "type_payment": "Loyer",
            "origin": "Locataire",
            "rental_id": 1
        }, follow_redirects=True)
        assert response.status_code == 200

    def test_create_rent(self, client, app):
        with client.session_transaction() as session:
            session["username"] = "test@test.fr"
            session["role"] = "admin"

        TestCreatePayment.create_test_entity(app)

        client.post("/finances/creer", data={
            "amount": 500,
            "payment_date": "2023-05-08",
            "observation": "test",
            "type_payment": "Loyer",
            "origin": "Locataire",
            "rental_id": 1
        }, follow_redirects=True)

        with app.app_context():
            try:
                rent_test = Rent.query.filter_by(payment_id=1).first()
            except Exception:
                rent_test = None
        assert rent_test is not None

    def test_create_rent_redirect(self, client, app):
        with client.session_transaction() as session:
            session["username"] = "test@test.fr"
            session["role"] = "admin"

        TestCreatePayment.create_test_entity(app)

        response = client.post("/finances/creer", data={
            "amount": 500,
            "payment_date": "2023-05-08",
            "observation": "test",
            "type_payment": "Loyer",
            "origin": "Locataire",
            "rental_id": 1
        }, follow_redirects=True)
        assert '<title>CoopImmoGestion-Finances</title>' in response.data.decode('utf-8')

    # Security deposit
    def test_send_data_security_deposit(self, client, app):
        with client.session_transaction() as session:
            session["username"] = "test@test.fr"
            session["role"] = "admin"

        TestCreatePayment.create_test_entity(app)

        response = client.post("/finances/creer", data={
            "amount": 500,
            "payment_date": "2023-05-08",
            "observation": "test",
            "type_payment": "Dépôt de garantie",
            "origin": "",
            "rental_id": 1
        }, follow_redirects=True)
        assert response.status_code == 200

    def test_create_security_deposit(self, client, app):
        with client.session_transaction() as session:
            session["username"] = "test@test.fr"
            session["role"] = "admin"

        TestCreatePayment.create_test_entity(app)

        client.post("/finances/creer", data={
            "amount": 500,
            "payment_date": "2023-05-08",
            "observation": "test",
            "type_payment": "Dépôt de garantie",
            "origin": "",
            "rental_id": 1
        }, follow_redirects=True)

        with app.app_context():
            try:
                security_deposit_test = SecurityDeposit.query.filter_by(payment_id=1).first()
            except Exception:
                security_deposit_test = None
        assert security_deposit_test is not None

    def test_create_security_deposit_redirect(self, client, app):
        with client.session_transaction() as session:
            session["username"] = "test@test.fr"
            session["role"] = "admin"

        TestCreatePayment.create_test_entity(app)

        response = client.post("/finances/creer", data={
            "amount": 500,
            "payment_date": "2023-05-08",
            "observation": "test",
            "type_payment": "Dépôt de garantie",
            "origin": "",
            "rental_id": 1
        }, follow_redirects=True)
        assert '<title>CoopImmoGestion-Finances</title>' in response.data.decode('utf-8')

    # Test create payments from rental controller
    # Rent
    def test_send_data_rental_rent(self, client, app):
        with client.session_transaction() as session:
            session["username"] = "test@test.fr"
            session["role"] = "admin"

        TestCreatePayment.create_test_entity(app)

        response = client.post("/locations/paiement/creer/1", data={
            "amount": 500,
            "payment_date": "2023-05-08",
            "observation": "test",
            "type_payment": "Loyer",
            "origin": "Locataire"
        }, follow_redirects=True)
        assert response.status_code == 200

    def test_create_rental_rent(self, client, app):
        with client.session_transaction() as session:
            session["username"] = "test@test.fr"
            session["role"] = "admin"

        TestCreatePayment.create_test_entity(app)

        client.post("/locations/paiement/creer/1", data={
            "amount": 500,
            "payment_date": "2023-05-08",
            "observation": "test",
            "type_payment": "Loyer",
            "origin": "Locataire"
        }, follow_redirects=True)

        with app.app_context():
            try:
                rent_test = Rent.query.filter_by(payment_id=1).first()
            except Exception:
                rent_test = None
        assert rent_test is not None

    def test_create_rental_rent_redirect(self, client, app):
        with client.session_transaction() as session:
            session["username"] = "test@test.fr"
            session["role"] = "admin"

        TestCreatePayment.create_test_entity(app)

        response = client.post("/locations/paiement/creer/1", data={
            "amount": 500,
            "payment_date": "2023-05-08",
            "observation": "test",
            "type_payment": "Loyer",
            "origin": "Locataire"
        }, follow_redirects=True)
        assert '<title>CoopImmoGestion-Locations</title>' in response.data.decode('utf-8')

    # Security deposit
    def test_send_data_rental_security_deposit(self, client, app):
        with client.session_transaction() as session:
            session["username"] = "test@test.fr"
            session["role"] = "admin"

        TestCreatePayment.create_test_entity(app)

        response = client.post("/locations/paiement/creer/1", data={
            "amount": 500,
            "payment_date": "2023-05-08",
            "observation": "test",
            "type_payment": "Dépôt de garantie",
            "origin": ""
        }, follow_redirects=True)
        assert response.status_code == 200

    def test_create_rental_security_deposit(self, client, app):
        with client.session_transaction() as session:
            session["username"] = "test@test.fr"
            session["role"] = "admin"

        TestCreatePayment.create_test_entity(app)

        client.post("/locations/paiement/creer/1", data={
            "amount": 500,
            "payment_date": "2023-05-08",
            "observation": "test",
            "type_payment": "Dépôt de garantie",
            "origin": ""
        }, follow_redirects=True)

        with app.app_context():
            try:
                security_deposit_test = SecurityDeposit.query.filter_by(payment_id=1).first()
            except Exception:
                security_deposit_test = None
        assert security_deposit_test is not None

    def test_create_rental_security_deposit_redirect(self, client, app):
        with client.session_transaction() as session:
            session["username"] = "test@test.fr"
            session["role"] = "admin"

        TestCreatePayment.create_test_entity(app)

        response = client.post("/locations/paiement/creer/1", data={
            "amount": 500,
            "payment_date": "2023-05-08",
            "observation": "test",
            "type_payment": "Dépôt de garantie",
            "origin": ""
        }, follow_redirects=True)
        assert '<title>CoopImmoGestion-Locations</title>' in response.data.decode('utf-8')

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
