from coopimmogestion.db.db import db
from datetime import datetime as dt
from coopimmogestion.models.Apartment import Apartment
from coopimmogestion.models.Tenant import Tenant
from coopimmogestion.models.Address import Address
from coopimmogestion.models.Rental import Rental


class TestUpdateRental:
    def test_send_data_update_rental(self, client, app):
        with client.session_transaction() as session:
            session["username"] = "test@test.fr"
            session["role"] = "admin"

        TestUpdateRental.create_test_entity(app)

        response = client.post("/locations/modifier/1", data={
            "start_date": "2023-04-09",
            "end_date": "2023-05-08",
            "tenant_id": 1,
            "apartment_id": 1
        }, follow_redirects=True)

        assert response.status_code == 200

    def test_update_rental(self, client, app):
        with client.session_transaction() as session:
            session["username"] = "test@test.fr"
            session["role"] = "admin"

        TestUpdateRental.create_test_entity(app)

        client.post("/locations/modifier/1", data={
            "start_date": "2023-04-09",
            "end_date": "2023-05-08",
            "tenant_id": 1,
            "apartment_id": 1
        }, follow_redirects=True)

        with app.app_context():
            with app.app_context():
                try:
                    rental_test = Rental.query.filter_by(start_date="2023-04-09").first()
                except Exception:
                    rental_test = None
            assert rental_test is not None

    def test_update_rental_redirect(self, client, app):
        with client.session_transaction() as session:
            session["username"] = "test@test.fr"
            session["role"] = "admin"

        TestUpdateRental.create_test_entity(app)

        response = client.post("/locations/modifier/1", data={
            "start_date": "2023-04-09",
            "end_date": "2023-05-08",
            "tenant_id": 1,
            "apartment_id": 1
        }, follow_redirects=True)

        assert '<title>CoopImmoGestion-Locations</title>' in response.data.decode('utf-8')

    def test_send_data_update_rental_tenant(self, client, app):
        with client.session_transaction() as session:
            session["username"] = "test@test.fr"
            session["role"] = "admin"

        TestUpdateRental.create_test_entity(app)

        response = client.post("/locations/locataire/modifier/1", data={
            "first_name": "test1",
            "last_name": "test",
            "birthday": "2023-04-08",
            "phone_number": "0000000001",
            "email": "test@test1.fr",
            "social_security_number": "test",
            "annual_salary": 30000.00,
            "balance": 0.00,
            "street_name": "test",
            "street_number": 1,
            "additional_address": "A",
            "zip_code": "00000",
            "city": "Test"
        }, follow_redirects=True)
        assert response.status_code == 200

    def test_update_rental_tenant(self, client, app):
        with client.session_transaction() as session:
            session["username"] = "test@test.fr"
            session["role"] = "admin"

        TestUpdateRental.create_test_entity(app)

        client.post("/locations/locataire/modifier/1", data={
            "first_name": "test1",
            "last_name": "test",
            "birthday": "2023-04-08",
            "phone_number": "0000000001",
            "email": "test@test1.fr",
            "social_security_number": "test",
            "annual_salary": 30000.00,
            "balance": 0.00,
            "street_name": "test",
            "street_number": 1,
            "additional_address": "A",
            "zip_code": "00000",
            "city": "Test"
        }, follow_redirects=True)

        with app.app_context():
            with app.app_context():
                try:
                    tenant_test = Tenant.query.filter_by(first_name="test1").first()
                except Exception:
                    tenant_test = None
            assert tenant_test is not None

    def test_update_rental_tenant_redirect(self, client, app):
        with client.session_transaction() as session:
            session["username"] = "test@test.fr"
            session["role"] = "admin"

        TestUpdateRental.create_test_entity(app)

        response = client.post("/locations/locataire/modifier/1", data={
            "first_name": "test1",
            "last_name": "test",
            "birthday": "2023-04-08",
            "phone_number": "0000000001",
            "email": "test@test1.fr",
            "social_security_number": "test",
            "annual_salary": 30000.00,
            "balance": 0.00,
            "street_name": "test",
            "street_number": 1,
            "additional_address": "A",
            "zip_code": "00000",
            "city": "Test"
        }, follow_redirects=True)
        assert '<title>CoopImmoGestion-Locations</title>' in response.data.decode('utf-8')

    def test_send_data_update_rental_apartment(self, client, app):
        with client.session_transaction() as session:
            session["username"] = "test@test.fr"
            session["role"] = "admin"

        TestUpdateRental.create_test_entity(app)

        response = client.post("/locations/appartement/modifier/1", data={
            "reference": "test1",
            "living_area": 150.333,
            "rooms": 5,
            "stage": 1,
            "outdoor": True,
            "rent": 200,
            "charge": 100,
            "security_deposit": 400,
            "street_name": "test",
            "street_number": 1,
            "additional_address": "A",
            "zip_code": "00000",
            "city": "Test"
        }, follow_redirects=True)
        assert response.status_code == 200

    def test_update_rental_apartment(self, client, app):
        with client.session_transaction() as session:
            session["username"] = "test@test.fr"
            session["role"] = "admin"

        TestUpdateRental.create_test_entity(app)

        client.post("/locations/appartement/modifier/1", data={
            "reference": "test1",
            "living_area": 150.333,
            "rooms": 5,
            "stage": 1,
            "outdoor": True,
            "rent": 200,
            "charge": 100,
            "security_deposit": 400,
            "street_name": "test",
            "street_number": 1,
            "additional_address": "A",
            "zip_code": "00000",
            "city": "Test"
        }, follow_redirects=True)

        with app.app_context():
            with app.app_context():
                try:
                    apartment_test = Apartment.query.filter_by(reference="test1").first()
                except Exception:
                    apartment_test = None
            assert apartment_test is not None

    def test_update_rental_apartment_redirect(self, client, app):
        with client.session_transaction() as session:
            session["username"] = "test@test.fr"
            session["role"] = "admin"

        TestUpdateRental.create_test_entity(app)

        response = client.post("/locations/appartement/modifier/1", data={
            "reference": "test1",
            "living_area": 150.333,
            "rooms": 5,
            "stage": 1,
            "outdoor": True,
            "rent": 200,
            "charge": 100,
            "security_deposit": 400,
            "street_name": "test",
            "street_number": 1,
            "additional_address": "A",
            "zip_code": "00000",
            "city": "Test"
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
