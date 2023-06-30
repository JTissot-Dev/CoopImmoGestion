![Cover](https://github.com/JeromeTissot69500/CoopImmoGestion/blob/OTH-Add-img-readme/img/Brand_logo2.jpg?raw=true)

<br>

## About The Project

<div align="center">
  <img src="https://github.com/JeromeTissot69500/CoopImmoGestion/blob/OTH-Add-img-readme/img/Index_view.jpg?raw=true">
</div>
CoopImmoGestion is a responsive web application allowing to make rental management easier, and have been developed as part of my training as a "concepteur, developpeur de solutions digitales".
<br>

### Built With

* ![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)
![Bootstrap](https://img.shields.io/badge/bootstrap-%238511FA.svg?style=for-the-badge&logo=bootstrap&logoColor=white)

* ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)

* ![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
<br>

## Getting starded
The following instructions will show you how to run it in your local environment.

### Prerequisites
Set up:
* <a href="https://www.python.org/downloads/release/python-3110/"> Python 3.11.0 </a>
* <a href="https://www.enterprisedb.com/downloads/postgres-postgresql-downloads"> PostgreSQL 15.3 </a>

### Installation
1. Clone the repository
   ```sh
   git clone https://github.com/JeromeTissot69500/CoopImmoGestion.git
   ```

2. Create python virtual environment in CoopImmoGestion folder
   ```sh
   python -m venv venvimmo
   ```

3. Activate virtual environment
   ```
   venvimmo/Scripts/activate
   ```

4. Install required package
   ```
   pip install -r requirements.txt
   ```

5. Create postgres database with pg Admin 
<div align="center">
  <img src="https://github.com/JeromeTissot69500/CoopImmoGestion/blob/OTH-Add-img-readme/img/pg_Admin_capture.jpg?raw=true">
</div>

6. Set the name and save
<div align="center">
  <img src="https://github.com/JeromeTissot69500/CoopImmoGestion/blob/OTH-Add-img-readme/img/pg_Admin_capture2.jpg?raw=true">
</div>

7. Set environment variable for the flask application
   ```
   export FLASK_APP=coopimmogestion
   ```

8. Upgrade database schema
   ```
   flask db upgrade
   ```

9. At this point, the application should be properly installed on your device, now, you juste have to run it !
   ```
   flask run
   ```

