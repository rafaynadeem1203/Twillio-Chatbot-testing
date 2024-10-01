from flask import Flask
from flask import Flask, jsonify
from flask_pymongo import pymongo

def connect():
    try:
        CONNECTION_STRING = "mongodb+srv://rafay:8jczBwnibR7kYejn@cluster0.nvqyp.mongodb.net/?retryWrites=true&w=majority"
        return  pymongo.MongoClient(CONNECTION_STRING)

    except Exception as e:
        print('Something went wrong!')
        print(str(e))
        return "Failed to connect to the database."
