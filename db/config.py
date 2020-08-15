import os

from flask import Flask
from flask_pymongo import PyMongo
from mongodb_migrations.cli import MigrationManager

import migrations

MONGO_DB = PyMongo()


def configure_mongo(app: Flask, py_mongo: PyMongo = MONGO_DB):
    app.config["MONGO_URI"] = os.environ.get("MONGODB_URI", default='mongodb://localhost:27017/mongo')
    py_mongo.init_app(app)
    # perform_migrations(app.config["MONGO_URI"])


def perform_migrations(mongo_url: str):
    manager = MigrationManager()
    manager.config.mongo_url = mongo_url
    manager.config.mongo_migrations_path = os.path.dirname(migrations.__file__)
    manager.run()
