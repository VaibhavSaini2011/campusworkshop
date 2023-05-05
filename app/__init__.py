"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chaaai2k728r8864nmug-a.oregon-postgres.render.com",
        database="to_do_betsol",
        user="to_do_betsol_user",
        password="j5oTUgspQw419XAbFdvGqrsUHOGFvyR5")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
