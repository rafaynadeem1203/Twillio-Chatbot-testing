from flask import jsonify
from bson import ObjectId
from datetime import datetime
from dateutil import parser

import requests
from utils.dbConfig import connect


def get_workorders(dbname):
    try:
        connect()
        client = connect()
        db = client.get_database(dbname)
        user_collection = db.workorders
        allWorkorders = list(user_collection.find({}))
        for item in allWorkorders:
            item['_id'] = str(item['_id'])

        print("All workorders are: ", allWorkorders)    
        #return jsonify({allWorkorders})
        client.close()
        return allWorkorders

    except Exception as e:
        print("Error fetching Workorders:", str(e))
        return "Internal Server Error", 500
        
        

def get_workorder_by_id(id,dbname):
    try:
        connect()
        client = connect()
        db = client.get_database(dbname)
        user_collection = db.workorders
        workorder_details = user_collection.find_one({"woID": int(id)})
        workorder_details["_id"]=str(workorder_details["_id"])
        client.close()
        
        if workorder_details:
            print("Workorder details are: ", workorder_details)
            workorder_details["_id"]=str(workorder_details["_id"])
            return workorder_details
        else:
            print("Workorder not found")
            return "Workorder not found"

    except Exception as e:
        print("Error fetching Workorder details:", str(e))
        return "Internal Server Error", 500

