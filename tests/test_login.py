from flask import session


class TestLogin:
    def test_access_login_status(self, client):
        response = client.get("/connexion")
        assert response.status_code == 200

    def test_access_login_data(self, client):
        response = client.get("/connexion")
        assert '<title>CoopImmoGestion-connexion</title>' in response.data.decode('utf-8')

    def test_login_success_status(self, client):
        response = client.post("/connexion", data={
            "email": "test@test.fr",
            "password": "Test2023*",
        }, follow_redirects=True)
        assert response.status_code == 200

    def test_login_success_session(self, client):
        with client:
            response = client.post("/connexion", data={
                "email": "test@test.fr",
                "password": "Test2023*"
            }, follow_redirects=True)
            assert session["username"] == "test@test.fr"

    def test_login_success_redirect(self, client):
        with client:
            response = client.post("/connexion", data={
                "email": "test@test.fr",
                "password": "Test2023*"
            }, follow_redirects=True)
            assert '<title>CoopImmoGestion-acceuil</title>' in response.data.decode('utf-8')

    def test_login_failed_status(self, client):
        response = client.post("/connexion", data={
            "email": "test_wrong_value",
            "password": "test_wrong_value"
        })
        assert response.status_code == 200

    def test_login_failed_session(self, client):
        with client:
            response = client.post("/connexion", data={
                "email": "test_wrong_value",
                "password": "test_wrong_value*"
            })
            assert session.get("username") is None

    def test_login_failed_data(self, client):
        response = client.post("/connexion", data={
            "email": "test_wrong_value",
            "password": "test_wrong_value"
        })
        assert '<title>CoopImmoGestion-connexion</title>' in response.data.decode('utf-8')




