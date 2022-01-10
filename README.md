# Two sum requests 
Django REST API for making requests for finding two numbers in a list which sum is equal to target integer number. Also for storing and deleting valid requests.
Used Python 3.8.10, Django 4.0.1, GRF 3.13.1, MySQL 2.1.0

### Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

### Clone

- Clone this repo to your local machine using `https://github.com/MariiaBurda/two_sum_requests.git`

### Setup

> create and activate virtual environment first

```shell
$ python3 -m venv venv
$ . venv/bin/activate
```

> install all needed packages

```shell
$ pip install -r requirements.txt
```

Setup database and create file with global variables 

  - Create MySQL database, user and password
  - Create secrets.json file in the root project folder (in the same level as manage.py and requirements.txt)
  - Generate secret key for the project
  - Add secret key, MySQL database name, user name and password to secrets.json

```shell
{
    "SECRET_KEY": "<your_secter_key>",
    "DB_NAME": "<your_db_name>",
    "DB_USER_NAME": "<your_db_user_name>",
    "DB_PASSWORD": "<your_db_user_password>"
}
```

> run django server

```shell
$ python manage.py runserver
```
### Test API urls

   - POST /api/two-sum/ - accepts a list of integers and target integer. In response return two indexes on numbers sum of which is equal to target (error if not)
     
     Example input:
     
     ```shell
      {
        "input": {
          "nums": [2,7,11,15],
          "target": 9
        }
      }
      ```
     
     Expected output:
     
     ```shell
      {
        "output": [0,1]
      }
      ```
      
   - GET /api/two-sum/ - returns a paginated list of all accepted valid requests.
         
   - GET /api/two-sum/?limit={}&page={} - use limit and page parameters to control pagination response.
         
   - GET /api/two-sum/{id} - specific result by id.
   
   - DELETE /api/two-sum/{id} - delete entity.
