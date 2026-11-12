# Stuart's Comic Shop

An e-commerce web app for a comic book store, built for CSE370 (Database Systems) at BRAC University. The project focuses on relational database design with MySQL and a Flask front end.

## Features

- User registration and profiles with loyalty points
- Product catalogue and product creation
- Orders: create an order and add products to it
- Product reviews
- ComicCon events that users can register for using loyalty points

## Tech stack

- **Backend:** Python, Flask, Flask-Login, Flask-WTF
- **Database:** MySQL (`mysql-connector`, `mysqlclient`)
- **Frontend:** HTML and CSS templates (Jinja2)

## Project structure

```
app/
├── __init__.py          # App factory
├── forms.py             # WTForms forms
├── models.py            # SQL queries for users, products, orders, reviews, events
└── routes/
    └── main_routes.py   # Page routes
run.py                   # Entry point
requirements.txt
```

## Getting started

```bash
pip install -r requirements.txt
python run.py
```

Create a MySQL database called `stuarts_comic_shop` and update the connection settings in `app/models.py` to match your local setup.
