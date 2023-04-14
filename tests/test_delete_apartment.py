from coopimmogestion.models.Apartment import Apartment
from coopimmogestion.db.db import db


class TestDeleteApartment:
    def test_access_delete_apartment(self, client):
        with client.session_transaction() as session:
            session["username"] = "test@test.fr"
            session["role"] = "admin"

        client.post("/appartements/creer", data={
            "reference": "test",
            "living_area": 150.333,
            "rooms": 5,
            "stage": 1,
            "outdoor": True,
            "street_name": "test",
            "street_number": 1,
            "additional_address": "A",
            "zip_code": "00000",
            "city": "Test"
        }, follow_redirects=True)

        response = client.get("/appartements/supprimer/1", follow_redirects=True)
        assert response.status_code == 200

    def test_delete_apartment(self, client, app):
        with client.session_transaction() as session:
            session["username"] = "test@test.fr"
            session["role"] = "admin"

        client.post("/appartements/creer", data={
            "reference": "test",
            "living_area": 150.333,
            "rooms": 5,
            "stage": 1,
            "outdoor": True,
            "street_name": "test",
            "street_number": 1,
            "additional_address": "A",
            "zip_code": "00000",
            "city": "Test"
        }, follow_redirects=True)

        client.get("/appartements/supprimer/1", follow_redirects=True)

        with app.app_context():
            with db.session.begin():
                try:
                    apartment_test = Apartment.query.filter_by(reference="test").first()
                except Exception:
                    apartment_test = None
            assert apartment_test is None

    def test_delete_apartment_redirect(self, client):
        with client.session_transaction() as session:
            session["username"] = "test@test.fr"
            session["role"] = "admin"

        client.post("/appartements/creer", data={
            "reference": "test",
            "living_area": 150.333,
            "rooms": 5,
            "stage": 1,
            "outdoor": True,
            "street_name": "test",
            "street_number": 1,
            "additional_address": "A",
            "zip_code": "00000",
            "city": "Test"
        }, follow_redirects=True)

        response = client.get("/appartements/supprimer/1", follow_redirects=True)
        assert '<title>CoopImmoGestion-appartements</title>' in response.data.decode('utf-8')