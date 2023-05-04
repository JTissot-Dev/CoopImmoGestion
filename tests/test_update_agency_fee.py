from coopimmogestion.models.AgencyFee import AgencyFee


class TestUpdateAgencyFee:
    def test_send_data_update_agency_fee(self, client):
        with client.session_transaction() as session:
            session["username"] = "test@test.fr"
            session["role"] = "admin"


        response = client.post("/finances/frais-agence/modifier", data={
            "rate": 0.09
        }, follow_redirects=True)
        assert response.status_code == 200

    def test_update_agency_fee(self, client, app):
        with client.session_transaction() as session:
            session["username"] = "test@test.fr"
            session["role"] = "admin"

        client.post("/finances/frais-agence/modifier", data={
            "rate": 0.09
        }, follow_redirects=True)

        with app.app_context():
            with app.app_context():
                try:
                    agency_fee_test = AgencyFee.query.filter_by(agency_fee_id=1).first()
                except Exception:
                    agency_fee_test = None
            assert agency_fee_test.rate == 0.09

    def test_update_agency_fee_redirect(self, client):
        with client.session_transaction() as session:
            session["username"] = "test@test.fr"
            session["role"] = "admin"

        response = client.post("/finances/frais-agence/modifier", data={
            "rate": 0.09
        }, follow_redirects=True)
        assert '<title>CoopImmoGestion-Finances</title>' in response.data.decode('utf-8')

