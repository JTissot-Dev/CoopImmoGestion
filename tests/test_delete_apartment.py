from coopimmogestion.models.Apartment import Apartment
from coopimmogestion.models.Address import Address
from coopimmogestion.db.db import db


class TestDeleteApartment:
    def test_access_delete_apartment(self, client, app):
        with client.session_transaction() as session:
            session["username"] = "test@test.fr"
            session["role"] = "admin"

        TestDeleteApartment.create_test_entity(app)

        response = client.get("/appartements/supprimer/1", follow_redirects=True)
        assert response.status_code == 200

    def test_delete_apartment(self, client, app):
        with client.session_transaction() as session:
            session["username"] = "test@test.fr"
            session["role"] = "admin"

        TestDeleteApartment.create_test_entity(app)

        client.get("/appartements/supprimer/1", follow_redirects=True)

        with app.app_context():
            with db.session.begin():
                try:
                    apartment_test = Apartment.query.filter_by(reference="test").first()
                except Exception:
                    apartment_test = None
            assert apartment_test is None

    def test_delete_apartment_redirect(self, client, app):
        with client.session_transaction() as session:
            session["username"] = "test@test.fr"
            session["role"] = "admin"

        TestDeleteApartment.create_test_entity(app)

        response = client.get("/appartements/supprimer/1", follow_redirects=True)
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
