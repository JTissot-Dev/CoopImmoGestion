from coopimmogestion.models.Inventory import Inventory
from coopimmogestion.db.db import db


class TestDeleteInventory:
    def test_access_delete_inventory(self, client):
        with client.session_transaction() as session:
            session["username"] = "test@test.fr"
            session["role"] = "admin"

        client.post("/appartements/creer", data={
            "reference": "test",
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

        client.post("/locataires/creer", data={
            "first_name": "test",
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

        client.post("/locations/creer", data={
            "start_date": "2023-04-08",
            "end_date": "2023-05-08",
            "tenant_id": 1,
            "apartment_id": 1
        }, follow_redirects=True)

        client.post("/etat-des-lieux/creer", data={
            "type_inv": "Entrée",
            "inventory_date": "2023-05-08",
            "observation": "test",
            "rental_id": 1
        }, follow_redirects=True)

        response = client.get("/etat-des-lieux/supprimer/1", follow_redirects=True)
        assert response.status_code == 200

    def test_delete_inventory(self, client, app):
        with client.session_transaction() as session:
            session["username"] = "test@test.fr"
            session["role"] = "admin"

        client.post("/appartements/creer", data={
            "reference": "test",
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

        client.post("/locataires/creer", data={
            "first_name": "test",
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

        client.post("/locations/creer", data={
            "start_date": "2023-04-08",
            "end_date": "2023-05-08",
            "tenant_id": 1,
            "apartment_id": 1
        }, follow_redirects=True)

        client.post("/etat-des-lieux/creer", data={
            "type_inv": "Entrée",
            "inventory_date": "2023-05-08",
            "observation": "test",
            "rental_id": 1
        }, follow_redirects=True)

        client.get("/etat-des-lieux/supprimer/1", follow_redirects=True)

        with app.app_context():
            with db.session.begin():
                try:
                    inventory_test = Inventory.query.filter_by(inventory_id=1).first()
                except Exception:
                    inventory_test = None
            assert inventory_test is None

    def test_delete_inventory_redirect(self, client):
        with client.session_transaction() as session:
            session["username"] = "test@test.fr"
            session["role"] = "admin"

        client.post("/appartements/creer", data={
            "reference": "test",
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

        client.post("/locataires/creer", data={
            "first_name": "test",
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

        client.post("/locations/creer", data={
            "start_date": "2023-04-08",
            "end_date": "2023-05-08",
            "tenant_id": 1,
            "apartment_id": 1
        }, follow_redirects=True)

        client.post("/etat-des-lieux/creer", data={
            "type_inv": "Entrée",
            "inventory_date": "2023-05-08",
            "observation": "test",
            "rental_id": 1
        }, follow_redirects=True)

        response = client.get("/etat-des-lieux/supprimer/1", follow_redirects=True)
        assert '<title>CoopImmoGestion-Etat des lieux</title>' in response.data.decode('utf-8')
