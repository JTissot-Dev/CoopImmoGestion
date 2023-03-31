
class TestLogout:
    def test_access_account_allowed_status(self, client):
        with client.session_transaction() as session:
            session["username"] == "test@test.fr"
            session["role"] == "admin"
            response = client.get("/comptes")
            assert response.status_code == 200

    def test_access_account_allowed_data(self, client):
        with client.session_transaction() as session:
            session["username"] == "test@test.fr"
            session["role"] == "admin"
            response = client.get("/comptes")
            assert '<title>CoopImmoGestion-comptes</title>' in response.data.decode('utf-8')

    def test_access_account_forbidden_status(self, client):
        with client.session_transaction() as session:
            session["username"] == "test@test.fr"
            session["role"] == "user"
            response = client.get("/comptes")
            assert response.status_code == 403

    def test_access_account_forbidden_data(self, client):
        with client.session_transaction() as session:
            session["username"] == "test@test.fr"
            session["role"] == "user"
            response = client.get("/comptes")
            assert '<title>CoopImmoGestion-redirection</title>' in response.data.decode('utf-8')
