from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.database import Database


def get_connection() -> MongoClient:
    # TODO Use environment variable
    return MongoClient('mongo', 27017)


def get_db() -> Database:
    # TODO Use environment variable
    return get_connection()['biasuncoverer']


def get_collection(name) -> Collection:
    return get_db().get_collection(name)
