from coopimmogestion.db.db import db
from datetime import datetime as dt
from coopimmogestion.models.Apartment import Apartment
from coopimmogestion.models.Tenant import Tenant
from coopimmogestion.models.Rental import Rental
from coopimmogestion.models.Address import Address
from coopimmogestion.models.Inventory import Inventory


class TestDeleteInventory:
    def test_access_delete_inventory(self, client, app):
        with client.session_transaction() as session:
            session["username"] = "test@test.fr"
            session["role"] = "admin"

        TestDeleteInventory.create_test_entity(app)

        response = client.get("/etat-des-lieux/supprimer/1", follow_redirects=True)
        assert response.status_code == 200

    def test_delete_inventory(self, client, app):
        with client.session_transaction() as session:
            session["username"] = "test@test.fr"
            session["role"] = "admin"

        TestDeleteInventory.create_test_entity(app)

        client.get("/etat-des-lieux/supprimer/1", follow_redirects=True)

        with app.app_context():
            with db.session.begin():
                try:
                    inventory_test = Inventory.query.filter_by(inventory_id=1).first()
                except Exception:
                    inventory_test = None
            assert inventory_test is None

    def test_delete_inventory_redirect(self, client, app):
        with client.session_transaction() as session:
            session["username"] = "test@test.fr"
            session["role"] = "admin"

        TestDeleteInventory.create_test_entity(app)

        response = client.get("/etat-des-lieux/supprimer/1", follow_redirects=True)
        assert '<title>CoopImmoGestion-Etat des lieux</title>' in response.data.decode('utf-8')

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

            inventory_test = Inventory(None, 'Entrée', dt.strptime('2023-01-01', '%Y-%m-%d'), 'Test', 1)
            db.session.add(inventory_test)
            db.session.commit()

