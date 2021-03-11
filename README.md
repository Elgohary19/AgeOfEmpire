# Age of Empire Run Guide
### Age of Empire is a small project where you can receive data from Age of Empire 2 [API](https://age-of-empires-2-api.herokuapp.com/docs/) and save in database and contain simple search using name


### You need Python == 3.7 to run this system
 
##### Open terminal then Clone the lastest repo using this command line
    git clone https://github.com/Elgohary19/AgeofEmpire.git
##### Install Virtualenv (if not installed)
    AgeofEmpire$ python3.7 -m pip install virtualenv 
##### Create your venv using this command:
    AgeofEmpire$ virtualenv --python python3.7 MyEnv  
##### Activate the virtualenv
    AgeofEmpire$ source MyEnv/bin/activate    
#### Install requirements
    AgeofEmpire$ pip install -r requirements.txt
##### Make migrations using following command line  
    AgeofEmpire$ python manage.py migrate
##### Run server to use site features (search in Database) 
    AgeofEmpire$ python manage.py runserver

Open a browser (Chrome or Firefox) and go to "[http://localhost:8000/](http://localhost:8000/)" Once you open you will
search field and table contain all data retrieved from " [Unit API](https://age-of-empires-2-api.herokuapp.com/api/v1/units) " 
if You want to find any unit name just search for it and our App will retrieve all matching data, if you searched for unit name 
not exist "No Result Found" message will appear to you. 