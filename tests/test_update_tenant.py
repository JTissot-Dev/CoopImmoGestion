from coopimmogestion.models.Tenant import Tenant
from coopimmogestion.db.db import db
from coopimmogestion.models.Address import Address
from datetime import datetime as dt


class TestUpdateTenant:
    def test_send_data_update_tenant(self, client, app):
        with client.session_transaction() as session:
            session["username"] = "test@test.fr"
            session["role"] = "admin"

        TestUpdateTenant.create_test_entity(app)

        response = client.post("/locataires/modifier/1", data={
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

    def test_update_tenant(self, client, app):
        with client.session_transaction() as session:
            session["username"] = "test@test.fr"
            session["role"] = "admin"

        TestUpdateTenant.create_test_entity(app)

        client.post("/locataires/modifier/1", data={
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

    def test_update_tenant_redirect(self, client, app):
        with client.session_transaction() as session:
            session["username"] = "test@test.fr"
            session["role"] = "admin"

        TestUpdateTenant.create_test_entity(app)

        response = client.post("/locataires/modifier/1", data={
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
        assert '<title>CoopImmoGestion-Locataires</title>' in response.data.decode('utf-8')

    @staticmethod
    def create_test_entity(app):
        with app.app_context():
            address_test: Address = Address(None, 'Test', 1, '', '00000', 'Test')
            db.session.add(address_test)
            db.session.commit()

            tenant_test: Tenant = Tenant(None, 'Test', 'Test', dt.now(), '0000000102', 'test@test.fr',
                                         address_test, 'Test', 30000)
            db.session.add(tenant_test)
            db.session.commit()