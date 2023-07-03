import sys
import psycopg2
import bcrypt
from datetime import datetime as dt

email: str = sys.argv[1]
password: str = sys.argv[2].encode('utf-8')


hash_password = bcrypt.hashpw(password, bcrypt.gensalt(14)).decode('utf-8')

try:
    conn = psycopg2.connect(host = 'localhost',
                            database = 'coopimmogestion',
                            user = 'postgres',
                            password = 'Development_2023',
                            port = '5432')

    cursor = conn.cursor()

    cursor.execute(
                    """
                    INSERT INTO public."Address" (address_id, street_name, street_number, additional_address, zip_code, city)
                    VALUES(1, 'Test street name', 0, 'Test addictional address', '00000', 'Test City')
                    """
                )       

    conn.commit()

    cursor.execute(
                    f"""
                    INSERT INTO public."AppUser" (first_name, last_name, birthday, phone_number, email, password, role, address_id)
                    VALUES('Test', 'Test', '2023-01-01', '0000000000', '{email}', '{hash_password}', 'admin', 1)
                    """
                )  

    conn.commit()
    conn.close()
    print('Succès de la création des données')
except Exception as e:
    print(e)
    sys.exit(1)

