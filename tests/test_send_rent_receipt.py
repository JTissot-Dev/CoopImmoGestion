from coopimmogestion.smtp.smtp import mail


class TestSendRentRecept:
    def test_send_rent_receipt_status(self, client):
        with client.session_transaction() as session:
            session["username"] = "test@test.fr"
            session["role"] = "admin"

        client.post("/appartements/creer", data={
            "reference": "test",
            "living_area": 150.333,
            "rooms": 5,
            "stage": 1,
            "outdoor": True,
            "rent": 200,
            "charge": 100,
            "security_deposit": 400,
            "street_name": "test",
            "street_number": 1,
            "additional_address": "A",
            "zip_code": "00000",
            "city": "Test"
        }, follow_redirects=True)

        client.post("/locataires/creer", data={
            "first_name": "test",
            "last_name": "test",
            "birthday": "2023-04-08",
            "phone_number": "0000000001",
            "email": "test@test1.fr",
            "social_security_number": "test",
            "annual_salary": 30000.00,
            "balance": 0.00,
            "street_name": "test",
            "street_number": 1,
            "additional_address": "A",
            "zip_code": "00000",
            "city": "Test"
        }, follow_redirects=True)

        client.post("/locations/creer", data={
            "start_date": "2023-04-08",
            "end_date": "2023-05-08",
            "tenant_id": 1,
            "apartment_id": 1
        }, follow_redirects=True)

        client.post("/finances/creer", data={
            "amount": 500,
            "payment_date": "2023-05-08",
            "observation": "test",
            "type_payment": "Loyer",
            "origin": "Locataire",
            "rental_id": 1
        }, follow_redirects=True)

        response = client.post("/finances/quittance-loyer", data={
            "rental_id": 1,
            "start_date": "2023-05-07",
            "end_date": "2023-05-09"
        }, follow_redirects=True)

        assert response.status_code == 200

    def test_send_rent_receipt(self, client, app):
        with app.app_context():
            with mail.record_messages() as outbox:
                mail.send_message(subject='testing',
                                  sender='coopimmogestion@gmail.com',
                                  body='test',
                                  recipients=['test@test.fr'])

                assert len(outbox) == 1
                assert outbox[0].subject == "testing"

    def test_send_rent_receipt_redirect(self, client):
        with client.session_transaction() as session:
            session["username"] = "test@test.fr"
            session["role"] = "admin"

        client.post("/appartements/creer", data={
            "reference": "test",
            "living_area": 150.333,
            "rooms": 5,
            "stage": 1,
            "outdoor": True,
            "rent": 200,
            "charge": 100,
            "security_deposit": 400,
            "street_name": "test",
            "street_number": 1,
            "additional_address": "A",
            "zip_code": "00000",
            "city": "Test"
        }, follow_redirects=True)

        client.post("/locataires/creer", data={
            "first_name": "test",
            "last_name": "test",
            "birthday": "2023-04-08",
            "phone_number": "0000000001",
            "email": "test@test1.fr",
            "social_security_number": "test",
            "annual_salary": 30000.00,
            "balance": 0.00,
            "street_name": "test",
            "street_number": 1,
            "additional_address": "A",
            "zip_code": "00000",
            "city": "Test"
        }, follow_redirects=True)

        client.post("/locations/creer", data={
            "start_date": "2023-04-08",
            "end_date": "2023-05-08",
            "tenant_id": 1,
            "apartment_id": 1
        }, follow_redirects=True)

        client.post("/finances/creer", data={
            "amount": 500,
            "payment_date": "2023-05-08",
            "observation": "test",
            "type_payment": "Loyer",
            "origin": "Locataire",
            "rental_id": 1
        }, follow_redirects=True)

        response = client.post("/finances/quittance-loyer", data={
            "rental_id": 1,
            "start_date": "2023-05-07",
            "end_date": "2023-05-09"
        }, follow_redirects=True)

        assert '<title>CoopImmoGestion-Finances</title>' in response.data.decode('utf-8')

