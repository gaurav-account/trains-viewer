# Train Departure Viewer

Train Departure Viewer has two parts:

1) Get stations

       Can be used to get list of stations along with repective station codes.
       API URL : http://localhost:8000/departures/v1/api/
       UI URL : http://localhost:8000/departures/


2) Get departures

       Can be used to get all train departures from a given station.
       API URL : http://localhost:8000/departures/v1/api/<Station_Code>
       UI URL : http://localhost:8000/departures/<Station_Code>



## Installation

Install Virtual Environment
```
py -m  pip install virtualenv
```

Create Virtual Environment

```bash
virtualenv venv -p `which python3`
```

Activate Virtual Environment

```bash
venv\Scripts\activate
```

URL for Target Web Service and Authentication Header Info is configurable in below file

```
config.properties

```
![image](https://user-images.githubusercontent.com/48081601/131246534-04fac2f2-28a0-4b9c-9dad-43478a83325a.png)


Install Requirement

```bash
py -m  pip install -r requirements-dev.txt
```

Run Tests
```
pytest --cov=departures --cov-report=html -s
```

Run Server

```
py manage.py runserver
```

## Test Coverage Report

![image](https://user-images.githubusercontent.com/48081601/131246479-22acdd11-6d60-4c42-b919-4f51701855ac.png)


## Testing Via Postman
#JSON as OUTPUT
1) Get All Stations

![image](https://user-images.githubusercontent.com/48081601/131247644-d878c17a-c21e-450b-ae3e-78366c5c8cc6.png)

2) Get All Departures

![image](https://user-images.githubusercontent.com/48081601/131247669-ab6fb84e-c5d6-47e3-8fa5-01598f23e16a.png)

## Testing Via Browser
#HTML as OUTPUT
1) Get All Stations

![image](https://user-images.githubusercontent.com/48081601/131247690-3a1353f0-8bdd-4092-bab3-6f755b804b01.png)
2) Get All Departures

![image](https://user-images.githubusercontent.com/48081601/131247709-8c6d2171-0649-4279-abc5-8dac80f53151.png)



## Contributing
Pull requests are welcome. 
