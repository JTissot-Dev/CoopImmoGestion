
class TestConsultApartment:
    def test_access_apartment_status(self, client):
        with client.session_transaction() as session:
            session["username"] = "test@test.fr"
            session["role"] = "admin"
        response = client.get("/appartements", follow_redirects=True)
        assert response.status_code == 200

    def test_access_apartment_data(self, client):
        with client.session_transaction() as session:
            session["username"] = "test@test.fr"
            session["role"] = "admin"
        response = client.get("/appartements", follow_redirects=True)
        assert '<title>CoopImmoGestion-appartements</title>' in response.data.decode('utf-8')

