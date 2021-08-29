# Train Departure Viewer

Train Departure Viewer has two parts:

1) Get stations

       Can be used to get list of stations along with repective station codes.             
       URL : http://localhost:8000/departures/


2) Get departures

       Can be used to get all train departures from a given station.
       URL : http://localhost:8000/departures/<Station_Code>
       Example : http://localhost:8000/departures/GVC



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

## Navigate to below URLs to Access Train Viewer Application

```
Home Page:
http://localhost:8000/departures/
To get departure for any station, click on the hyperlink on station code
http://localhost:8000/departures/<station_code>
```
## Test Coverage Report

![image](https://user-images.githubusercontent.com/48081601/131246479-22acdd11-6d60-4c42-b919-4f51701855ac.png)



## Contributing
Pull requests are welcome. 
