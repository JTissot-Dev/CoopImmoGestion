from coopimmogestion.models.AppUser import AppUser


class TestCreateAccount:
    def test_send_data_update_user_account(self, client):
        with client.session_transaction() as session:
            session["username"] = "test@test.fr"
            session["role"] = "admin"

        response = client.post("/comptes/modifier", data={
            "person_id": 1,
            "first_name": "test",
            "last_name": "test",
            "birthday": "2023-04-08",
            "phone_number": "0000000001",
            "email": "test@test1.fr",
            "role": "user",
            "password": "Test2000*",
            "street_name": "test",
            "street_number": 1,
            "additional_address": "A",
            "zip_code": "00000",
            "city": "Test"
        }, follow_redirects=True)
        assert response.status_code == 200

    def test_update_user_account(self, client, app):
        with client.session_transaction() as session:
            session["username"] = "test@test.fr"
            session["role"] = "admin"

        client.post("/comptes/modifier", data={
            "person_id": 1,
            "first_name": "test",
            "last_name": "test",
            "birthday": "2023-04-08",
            "phone_number": "0000000001",
            "email": "test@test1.fr",
            "role": "user",
            "password": "Test2000*",
            "street_name": "test",
            "street_number": 1,
            "additional_address": "A",
            "zip_code": "00000",
            "city": "Test"
        }, follow_redirects=True)

        with app.app_context():
            try:
                user_test = AppUser.query.filter_by(person_id=1).first()
            except Exception:
                user_test = None
        assert user_test is not None
        assert user_test.email == "test@test1.fr"

    def test_update_user_account_redirect(self, client):
        with client.session_transaction() as session:
            session["username"] = "test@test.fr"
            session["role"] = "admin"

        response = client.post("/comptes/modifier", data={
            "person_id": 1,
            "first_name": "test",
            "last_name": "test",
            "birthday": "2023-04-08",
            "phone_number": "0000000001",
            "email": "test@test1.fr",
            "role": "user",
            "password": "Test2000*",
            "street_name": "test",
            "street_number": 1,
            "additional_address": "A",
            "zip_code": "00000",
            "city": "Test"
        }, follow_redirects=True)
        assert '<title>CoopImmoGestion-comptes</title>' in response.data.decode('utf-8')