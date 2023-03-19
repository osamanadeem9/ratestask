# Task Implementation
## Frameworks/Libraries Used

For the task, I have avoided using lots of third party libraries. The repository uses only the very necessary libraries. The following libraries have been used:

* Flask
* pytest
* psycopg2
* python-dotenv

# To be Noted
* The implemented code has >90% test coverage.
* The code can be run both locally and using docker-compose.
* Most of the querying has been done using SQL (rather than using python loops or conditionals, which are rather simpler) to demonstrate SQL expertise as demanded in the task (inferenced from GitHub Readme file).
# API Details
Here are the details regarding the usage of implemented rates API.

## Required Parameters
The API uses GET Request to serve data to users. It requires the following parameters (not optional).
* date_from
* date_to
* origin
* destination

The dates should be written in the format *YYYY-MM-DD*. All the parameters must be non-null.

## Response Received
A list containing the average prices for each day on a route between port codes origin and destination, like below.
```json
[
    {
        "day": "2016-01-01",
        "average_price": 468
    },
    ...
]
```

## How to Run
The program can be run using the following commands

1. Make sure that you have Python, Git and pip installed on your PC.

2. Then clone the git repo to your preferred folder using cmd.
```cmd
git clone https://github.com/osamanadeem9/ratestask
```

3. Navigate to the *ratestask* folder
```cmd
cd ratestask
```

4. Install requirements for the project using
```cmd
pip install -r web/requirements.txt
```

5. Run tests using PyCharm, or by typing pytest
```cmd
pytest
```

6. Start the Flask app using python
```cmd
python web/app.py
```

7. Alternatively, you may also run the app using Docker Compose commands, as below:
```cmd
docker compose up -d db
```
```cmd
docker compose up --build web
```
```cmd
docker ps -a    # check if both container are up and running
```

8. For a sample request, either open this [link](http://127.0.0.1/rates/?date_from=2016-01-01&date_to=2016-01-10&origin=CNSGH&destination=north_europe_main) or head on to a new cmd terminal and enter the following:
```cmd
curl "http://127.0.0.1/rates/?date_from=2016-01-01&date_to=2016-01-10&origin=CNSGH&destination=north_europe_main"
```
9. The reponse is shown in the screenshot below:
<p align="center">
<img src="/outputs/s1.PNG" width="600" height="322" />
<!-- <img src = "/outputs/s1.PNG"> -->
</p>

# Working:
1. Running tests:
<p align="center">
<img src="/outputs/s5.PNG" width="600" height="322" />
</p>

2. Running locally using python command:
<p align="center">
<img src="/outputs/s2.PNG" width="600" height="322" />
</p>
3. Running using docker compose:
<p align="center">
<img src="/outputs/s3.PNG" width="600" height="322" />
</p>
<p align="center">
<img src="/outputs/s4.PNG" width="600" height="322" />
</p>


# Xeneta's Explanation:
## Data definition

We are providing you with a small set of simplified real-world data. A
database dump is provided that includes the following information:

### Ports

Information about ports, including:

* 5-character port code
* Port name
* Slug describing which region the port belongs to

### Regions

A hierarchy of regions, including:

* Slug - a machine-readable form of the region name
* The name of the region
* Slug describing which parent region the region belongs to

Note that a region can have both ports and regions as children, and the region
tree does not have a fixed depth.

### Prices

Individual daily prices between ports, in USD.

* 5-character origin port code
* 5-character destination port code
* The day for which the price is valid
* The price in USD

## Assignment: HTTP-based API

Develop an [HTTP-based API](#task-1-http-based-api) capable of handling the GET request described below. Our stack is based on Flask, but you are free to choose any Python framework you like. All data returned is expected to be in JSON format. Please demonstrate your knowledge of SQL (as opposed to using ORM querying tools).


Implement an API endpoint that takes the following parameters:

* date_from
* date_to
* origin
* destination

and returns a list with the average prices for each day on a route between port codes *origin* and *destination*. Return an empty value (JSON null) for days on which there are less than 3 prices in total.

Both the *origin, destination* params accept either port codes or region slugs, making it possible to query for average prices per day between geographic groups of ports.

    curl "http://127.0.0.1/rates?date_from=2016-01-01&date_to=2016-01-10&origin=CNSGH&destination=north_europe_main"

    [
        {
            "day": "2016-01-01",
            "average_price": 1112
        },
        {
            "day": "2016-01-02",
            "average_price": 1112
        },
        {
            "day": "2016-01-03",
            "average_price": null
        },
        ...
    ]

## Requirements

* Write the solution using Python and SQL, you can use an ORM but please
  demonstrate some raw SQL

* Keep your solution in a Version Control System of your
  choice. *Provide the solution as a public repository that can be
  easily cloned by our development team.*

* Provide any instructions needed to set up the system in `README.md`.

* Ensure the API handles errors and edge cases properly.

* Use dates in YYYY-MM-DD format for the API. There is no need for more
  complicated date processing.

## Extra details

* It usually takes 2 - 6 hours to complete this task for a developer with 2+ years of experience in building APIs with Python and SQL.

* Our key evaluation criteria:
    - Ease of setup and testing
    - Code clarity and simplicity
    - Comments where appropriate
    - Code organisation
    - Tests

* You are encouraged to modify or extend the database schema if you think a different model fits the task better.

* If you have any questions, please don't hesitate to contact us

* Please let us know how much time you spent on the task, and of any difficulties that you ran into.


## Initial setup

We have provided a simple Docker setup for you, which will start a
PostgreSQL instance populated with the assignment data. You don't have
to use it, but you might find it convenient. If you decide to use
something else, make sure to include instructions on how to set it up.

You can execute the provided Dockerfile by running:

```bash
docker build -t ratestask .
```

This will create a container with the name *ratestask*, which you can
start in the following way:

```bash
docker run -p 0.0.0.0:5432:5432 --name ratestask ratestask
```

You can connect to the exposed Postgres instance on the Docker host IP address,
usually *127.0.0.1* or *172.17.0.1*. It is started with the default user `postgres` and `ratestask` password.

```bash
PGPASSWORD=ratestask psql -h 127.0.0.1 -U postgres
```

alternatively, use `docker exec` if you do not have `psql` installed:

```bash
docker exec -e PGPASSWORD=ratestask -it ratestask psql -U postgres
```

Keep in mind that any data written in the Docker container will
disappear when it shuts down. The next time you run it, it will start
with a clean state.
