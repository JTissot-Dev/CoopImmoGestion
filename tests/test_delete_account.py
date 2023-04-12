from coopimmogestion.models.AppUser import AppUser
from coopimmogestion.db.db import db


class TestDeleteAccount:
    def test_access_delete_user_account(self, client):
        with client.session_transaction() as session:
            session["username"] = "test@test.fr"
            session["role"] = "admin"

        response = client.get("/comptes/supprimer/1", follow_redirects=True)
        assert response.status_code == 200

    def test_delete_user_account(self, client, app):
        with client.session_transaction() as session:
            session["username"] = "test@test.fr"
            session["role"] = "admin"

        client.get("/comptes/supprimer/1", follow_redirects=True)

        with app.app_context():
            with db.session.begin():
                try:
                    user_test = AppUser.query.filter_by(person_id=1).first()
                except Exception:
                    user_test = None
            assert user_test is None

    def test_delete_user_account_redirect(self, client):
        with client.session_transaction() as session:
            session["username"] = "test@test.fr"
            session["role"] = "admin"

        response = client.get("/comptes/supprimer/1", follow_redirects=True)
        assert '<title>CoopImmoGestion-comptes</title>' in response.data.decode('utf-8')