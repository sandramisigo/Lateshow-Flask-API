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
3. Install Depe…