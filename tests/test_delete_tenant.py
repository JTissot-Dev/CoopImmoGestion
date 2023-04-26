from coopimmogestion.models.Tenant import Tenant
from coopimmogestion.db.db import db
from coopimmogestion.models.Address import Address
from datetime import datetime as dt


class TestDeleteTenant:
    def test_access_delete_tenant(self, client, app):
        with client.session_transaction() as session:
            session["username"] = "test@test.fr"
            session["role"] = "admin"

        TestDeleteTenant.create_test_entity(app)

        response = client.get("/locataires/supprimer/1", follow_redirects=True)
        assert response.status_code == 200

    def test_delete_tenant(self, client, app):
        with client.session_transaction() as session:
            session["username"] = "test@test.fr"
            session["role"] = "admin"

        TestDeleteTenant.create_test_entity(app)

        client.get("/locataires/supprimer/1", follow_redirects=True)

        with app.app_context():
            with db.session.begin():
                try:
                    tenant_test = Tenant.query.filter_by(first_name="test1").first()
                except Exception:
                    tenant_test = None
            assert tenant_test is None

    def test_delete_tenant_redirect(self, client, app):
        with client.session_transaction() as session:
            session["username"] = "test@test.fr"
            session["role"] = "admin"

        TestDeleteTenant.create_test_entity(app)

        response = client.get("/locataires/supprimer/1", follow_redirects=True)
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
