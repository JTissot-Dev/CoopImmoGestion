from coopimmogestion.db.db import db
from coopimmogestion.models.Apartment import Apartment
from coopimmogestion.models.Address import Address


class TestUpdateApartment:
    def test_send_data_update_apartment(self, client, app):
        with client.session_transaction() as session:
            session["username"] = "test@test.fr"
            session["role"] = "admin"

        TestUpdateApartment.create_test_entity(app)

        response = client.post("/appartements/modifier/1", data={
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

    def test_update_apartment(self, client, app):
        with client.session_transaction() as session:
            session["username"] = "test@test.fr"
            session["role"] = "admin"

        TestUpdateApartment.create_test_entity(app)

        client.post("/appartements/modifier/1", data={
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

    def test_update_apartment_redirect(self, client, app):
        with client.session_transaction() as session:
            session["username"] = "test@test.fr"
            session["role"] = "admin"

        TestUpdateApartment.create_test_entity(app)

        response = client.post("/appartements/modifier/1", data={
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
        assert '<title>CoopImmoGestion-appartements</title>' in response.data.decode('utf-8')

    @staticmethod
    def create_test_entity(app):
        with app.app_context():
            address_test: Address = Address(None, 'Test', 1, '', '00000', 'Test')
            db.session.add(address_test)
            db.session.commit()

            apartment_test: Apartment = Apartment(None, 'Apartement-test', 150, 5, address_test,
                                                  2, True, 400, 100, 700)
            db.session.add(apartment_test)
            db.session.commit()
