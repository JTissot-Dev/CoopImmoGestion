from coopimmogestion.db.db import db
from datetime import datetime as dt
from coopimmogestion.models.Apartment import Apartment
from coopimmogestion.models.Tenant import Tenant
from coopimmogestion.models.Address import Address
from coopimmogestion.models.Rental import Rental


class TestCreateRental:
    def test_send_data_rental(self, client, app):
        with client.session_transaction() as session:
            session["username"] = "test@test.fr"
            session["role"] = "admin"

        TestCreateRental.create_test_entity(app)

        response = client.post("/locations/creer", data={
            "start_date": "2023-04-08",
            "end_date": "2023-05-08",
            "tenant_id": 1,
            "apartment_id": 1
        }, follow_redirects=True)
        assert response.status_code == 200

    def test_create_rental(self, client, app):
        with client.session_transaction() as session:
            session["username"] = "test@test.fr"
            session["role"] = "admin"

        TestCreateRental.create_test_entity(app)

        client.post("/locations/creer", data={
            "start_date": "2023-04-08",
            "end_date": "2023-05-08",
            "tenant_id": 1,
            "apartment_id": 1
        }, follow_redirects=True)

        with app.app_context():
            try:
                rental_test = Rental.query.filter_by(rental_id=1).first()
            except Exception:
                rental_test = None
        assert rental_test is not None

    def test_create_rental_redirect(self, client, app):
        with client.session_transaction() as session:
            session["username"] = "test@test.fr"
            session["role"] = "admin"

        TestCreateRental.create_test_entity(app)

        response = client.post("/locations/creer", data={
            "start_date": "2023-04-08",
            "end_date": "2023-05-08",
            "tenant_id": 1,
            "apartment_id": 1
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
