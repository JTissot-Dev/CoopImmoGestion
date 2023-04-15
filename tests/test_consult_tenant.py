
class TestConsultTenant:
    def test_access_tenant_status(self, client):
        with client.session_transaction() as session:
            session["username"] = "test@test.fr"
            session["role"] = "admin"
        response = client.get("/locataires", follow_redirects=True)
        assert response.status_code == 200

    def test_access_tenant_data(self, client):
        with client.session_transaction() as session:
            session["username"] = "test@test.fr"
            session["role"] = "admin"
        response = client.get("/locataires", follow_redirects=True)
        assert '<title>CoopImmoGestion-Locataires</title>' in response.data.decode('utf-8')

