
class TestConsultRental:
    def test_access_rental_status(self, client):
        with client.session_transaction() as session:
            session["username"] = "test@test.fr"
            session["role"] = "admin"
        response = client.get("/locations", follow_redirects=True)
        assert response.status_code == 200

    def test_access_rental_data(self, client):
        with client.session_transaction() as session:
            session["username"] = "test@test.fr"
            session["role"] = "admin"
        response = client.get("/locations", follow_redirects=True)
        assert '<title>CoopImmoGestion-Locations</title>' in response.data.decode('utf-8')

