![Cover](https://github.com/JeromeTissot69500/CoopImmoGestion/blob/OTH-Add-img-readme/img/Brand_logo2.jpg?raw=true)

<br>

## About The Project

<br>
<br>
<div align="center">
  <img src="https://github.com/JeromeTissot69500/CoopImmoGestion/blob/OTH-Add-img-readme/img/Index_view.jpg?raw=true" width="90%">
</div>
<br>
<br>
CoopImmoGestion is a responsive web application allowing to make rental management easier, and have been developed as part of my training as a "Concepteur, développeur de solutions digitales".
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

5. Before the nexts instructions, please insure that your postgres password matche with the password setting in database URI of the development config and the connexion password setting in create data file.

* _coopimmogestion/config/DevelopmentConfig.py_
&nbsp; <img src="https://github.com/JeromeTissot69500/CoopImmoGestion/blob/OTH-Add-img-readme/img/Dev_config_capture.jpg?raw=true" width="80%">
<br>

* _coopimmogestion/db/create_data.py_
&nbsp; <img src="https://github.com/JeromeTissot69500/CoopImmoGestion/blob/OTH-Add-img-readme/img/Create_data_capture.jpg" width="80%">
<br>

6. Create postgres database with pg Admin
<div align="center">
  <img src="https://github.com/JeromeTissot69500/CoopImmoGestion/blob/OTH-Add-img-readme/img/pg_Admin_capture.jpg?raw=true" width="90%">
</div>

7. Set the name and save
<div align="center">
  <img src="https://github.com/JeromeTissot69500/CoopImmoGestion/blob/OTH-Add-img-readme/img/pg_Admin_capture2.jpg?raw=true" width="90%">
</div>

8. Set environment variable for the flask app
   ```
   export FLASK_APP=coopimmogestion
   ```

9. Upgrade database schema
   ```
   flask db upgrade
   ```

1. At this point, the app should be properly installed on your device, now, you juste have to run it !
   ```
   flask run
   ```


## Usage

It's time to test the app, but before that, you need to follow somme additional steps.

### First connexion

To access the app, you'll need a username and a password, so, you have to create a first user in database.
<br>
<br>
<div align="center">
  <img src="https://github.com/JeromeTissot69500/CoopImmoGestion/blob/OTH-Add-img-readme/img/Login_view.jpg?raw=true" width="90%">
</div>
<br>
<br>

1. Create a first user in database
   
    _Specifie email address in first argument and password in second argument_
    ```
    python coopimmogestion/db/create_data.py test@test.com initUser*
    ```

### Handling

<p>You can now testing the full application, for a better handling, please refer to the <a href="https://drive.google.com/file/d/1Mcj-lSemjnrF0MeqdqLluUgZBjacuFEh/view?usp=sharing)https://drive.google.com/file/d/1Mcj-lSemjnrF0MeqdqLluUgZBjacuFEh/view?usp=sharing">Documentation</a></p>

## Contact

Jérôme Tissot - jerome.tissot@lamache.org
