
class TestConsultInventory:
    def test_access_inventory_status(self, client):
        with client.session_transaction() as session:
            session["username"] = "test@test.fr"
            session["role"] = "admin"
        response = client.get("/etat-des-lieux", follow_redirects=True)
        assert response.status_code == 200

    def test_access_inventory_data(self, client):
        with client.session_transaction() as session:
            session["username"] = "test@test.fr"
            session["role"] = "admin"
        response = client.get("/etat-des-lieux", follow_redirects=True)
        assert '<title>CoopImmoGestion-Etat des lieux</title>' in response.data.decode('utf-8')

