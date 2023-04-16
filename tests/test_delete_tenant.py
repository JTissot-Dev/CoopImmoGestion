from coopimmogestion.models.Tenant import Tenant
from coopimmogestion.db.db import db


class TestDeleteTenant:
    def test_access_delete_tenant(self, client):
        with client.session_transaction() as session:
            session["username"] = "test@test.fr"
            session["role"] = "admin"

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

        response = client.get("/locataires/supprimer/1", follow_redirects=True)
        assert response.status_code == 200

    def test_delete_tenant(self, client, app):
        with client.session_transaction() as session:
            session["username"] = "test@test.fr"
            session["role"] = "admin"

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

        client.get("/locataires/supprimer/1", follow_redirects=True)

        with app.app_context():
            with db.session.begin():
                try:
                    tenant_test = Tenant.query.filter_by(first_name="test1").first()
                except Exception:
                    tenant_test = None
            assert tenant_test is None

    def test_delete_tenant_redirect(self, client):
        with client.session_transaction() as session:
            session["username"] = "test@test.fr"
            session["role"] = "admin"

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

        response = client.get("/locataires/supprimer/1", follow_redirects=True)
        assert '<title>CoopImmoGestion-Locataires</title>' in response.data.decode('utf-8')
