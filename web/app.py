"""Simple API for performing basic mathematical operations.
-------------------------------------------------------------

API that takes two inputs as JSON and return data after calculation.
These calculations are just simply +, -, *, /

Note: This API work under POST request

@author Hamza Arain
@version 0.0.1v
@date 25 October 2020

"""


# import modules
from flask import Flask, jsonify, request
from flask_restful import Api, Resource

import os

from pymongo import MongoClient


class Visit(Resource):
    """
    Increament in no. of visitors
    """
    def get(self):
        prev_num = UserNum.find({})[0]['num_of_users']
        new_num = prev_num + 1
        UserNum.update({}, {"$set":{"num_of_users":new_num}})
        return str("Hello user " + str(new_num))


class Tool():
    """
    1. Check post data
    2. x & y resource data
    3. JSON return msg
    """
    def checkPostedData(self, postedData, functionName):
        """Check POST code data.
        200 > OK
        301 > Missing resource
        302 > if y == 0
        """
        if (functionName == "add" or functionName == "subtract" or functionName == "multiply"):
            if "x" not in postedData or "y" not in postedData:
                return 301 #Missing parameter
            else:
                return 200
        elif (functionName == "division"):
            if "x" not in postedData or "y" not in postedData:
                return 301
            elif int(postedData["y"])==0:
                return 302
            else:
                return 200

    def x_y_output(self, postedData, functionName):  
        """Return x & y if status code is 200"""      
        #Step 1: Get posted data:
        postedData = request.get_json()

        #Steb 1b: Verify validity of posted data
        status_code = self.checkPostedData(postedData, functionName)
        if (status_code!=200 and functionName!="divide"):
            retJson = {
                "Message": "An error happened",
                "Status Code":status_code
            }
            return jsonify(retJson)

        # #If i am here, then status_code == 200
        x = int(postedData["x"])
        y = int(postedData["y"])
        return x, y

    def JSONOutputMessage(self, output):
        """Return status code 200 & output"""
        retMap = {
            'Message': output,
            'Status Code': 200
        }
        return jsonify(retMap)



# ###########################################################
# #######################  API Class ########################
# ###########################################################    



class Add(Resource):
    """Adding from POST request"""
    def post(self):
        """resouce Add was requested using the method POST"""

        # Step 1: Get posted data:
        postedData = request.get_json()
        
        t = Tool()

        # Step 2: Add the posted data
        x, y = t.x_y_output(postedData, "add")
         
        ret = x + y
        return t.JSONOutputMessage(ret)

class Subtract(Resource):
    """Subtraction from POST request"""
    def post(self):
        """resouce Subtract was requested using the method POST"""
        # Step 1: Get posted data:
        postedData = request.get_json()
        
        t = Tool()

        # Step 2: Add the posted data
        x, y = t.x_y_output(postedData, "subtract")
         
        ret = x - y
        return t.JSONOutputMessage(ret)


class Multiply(Resource):
    """Multiplication from POST request"""
    def post(self):
        """resouce Multiply was requested using the method POST"""
        # Step 1: Get posted data:
        postedData = request.get_json()
        
        t = Tool()

        # Step 2: Add the posted data
        x, y = t.x_y_output(postedData, "multiply")
         
        ret = x * y
        return t.JSONOutputMessage(ret)

class Divide(Resource):
    """Divide from POST request"""
    def post(self):
        """resouce Divide was requested using the method POST"""
        # Step 1: Get posted data:
        t = Tool()

        postedData = request.get_json()

        # Step 2: Add the posted data
        x, y = t.x_y_output(postedData, "divide")
         
        ret = (x*1.0)/y
        return t.JSONOutputMessage(ret)




# ###########################################################
# ##################### Run Application #####################
# ###########################################################


# Database connection
# # "db" is same as written in web Dockerfile
# # "27017" is default port for MongoDB 
client = MongoClient("mongodb://db:27017")  
db = client.aNewDB      # Create database
UserNum = db["UserNum"] # Create collection

# Make initial value first time
UserNum.insert({
    'num_of_users':0
})

# App & API creation
app = Flask(__name__)
api = Api(app)

# API paths
api.add_resource(Add, "/add")
api.add_resource(Subtract, "/sub")
api.add_resource(Multiply, "/mul")
api.add_resource(Divide, "/div")
api.add_resource(Visit, "/hello")

# GET route
@app.route('/')
def hello_world():        
    return "Hello World!"

# Run application
if __name__=="__main__":
    # app.run(debug=True)
    app.run(host="0.0.0.0")