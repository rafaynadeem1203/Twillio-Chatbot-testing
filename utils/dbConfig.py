from flask import Flask
from flask import Flask, jsonify
from flask_pymongo import pymongo

def connect():
    try:
        CONNECTION_STRING = "mongodb://localhost:27017"
        return  pymongo.MongoClient(CONNECTION_STRING)

    except Exception as e:
        print('Something went wrong!')
        print(str(e))
        return "Failed to connect to the database."
