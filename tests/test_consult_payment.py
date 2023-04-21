
class TestConsultPayment:
    def test_access_payment_status(self, client):
        with client.session_transaction() as session:
            session["username"] = "test@test.fr"
            session["role"] = "admin"
        response = client.get("/finances", follow_redirects=True)
        assert response.status_code == 200

    def test_access_payment_data(self, client):
        with client.session_transaction() as session:
            session["username"] = "test@test.fr"
            session["role"] = "admin"
        response = client.get("/finances", follow_redirects=True)
        assert '<title>CoopImmoGestion-Finances</title>' in response.data.decode('utf-8')


