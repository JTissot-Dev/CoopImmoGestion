
class TestAccountBalances:
    def test_access_account_balances(self, client):
        with client.session_transaction() as session:
            session["username"] = "test@test.fr"
            session["role"] = "admin"
        response = client.get("/finances/billan-des-comptes", follow_redirects=True)
        assert response.status_code == 200

    def test_access_account_balances_data(self, client):
        with client.session_transaction() as session:
            session["username"] = "test@test.fr"
            session["role"] = "admin"
        response = client.get("/finances/billan-des-comptes", follow_redirects=True)
        assert '<title>CoopImmoGestion-Bilan-des-comptes</title>' in response.data.decode('utf-8')


