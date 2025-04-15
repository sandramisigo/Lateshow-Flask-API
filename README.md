# Late Show Flask API

This project is a Flask-based RESTful API that manages episodes, guests, and guest appearances on the Late Show. It supports viewing episodes, managing guests, and recording guest appearances with ratings.


## Features

- View all Late Show episodes
- View specific episode by ID
- View all guests
- Add a guest appearance with a rating (1–5)
- Validations and error handling
- Cascade deletes for related appearances
- Seed database from CSV file


## Tech Stack

- Python 3.10+
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- SQLite (for development)
- Postman (for API testing)


## Setup Instructions

### 1. Clone the Repository


git clone `git@github.com:sandramisigo/Lateshow-Flask-API.git`
cd lateshow
2. Create a Virtual Environment
3. Install Dependencies
pip install Flask Flask-SQLAlchemy Flask-Migrate

4. Set Up the Database

flask db init
flask db migrate -m "Initial migration."
flask db upgrade

5. Seed the Database
Make sure seed.csv is present in the root folder. Then:

python seed.py

Running the App

python app.py

By default, the app runs on: http://127.0.0.1:5000

API Endpoints
 Episodes
GET /episodes
Returns all episodes.

GET /episodes/<id>
Returns one episode with its guest appearances.

 Guests
GET /guests
Returns all guests.

 Appearances
POST /appearances
Create a new appearance. JSON Body:

## Contributing
* Fork the repository

* Create a new branch

* Commit your changes

* Open a pull request

## Author
Sandra Misigo

## Licence
MIT License