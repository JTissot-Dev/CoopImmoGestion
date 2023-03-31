from flask import session


class TestLogout:
    def test_access_logout_status(self, client):
        response = client.get("/deconnexion")
        assert response.status_code == 200

    def test_access_logout_data(self, client):
        response = client.get("/deconnexion")
        assert '<title>CoopImmoGestion-connexion</title>' in response.data.decode('utf-8')

    def test_logout_session(self, client):
        with client:
            client.get("/deconnexion")
            assert len(session) == 0

