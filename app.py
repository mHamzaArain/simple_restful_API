from flask import Flask, jsonify, request
from flask_restful import Api, Resource


app = Flask(__name__)
api = Api(app)

class Tool():
    def checkPostedData(self, postedData, functionName):
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
        #Step 1: Get posted data:
        postedData = request.get_json()


        #Steb 1b: Verify validity of posted data
        status_code = self.checkPostedData(postedData, functionName)
        if (status_code!=200):
            retJson = {
                "Message": "An error happened",
                "Status Code":status_code
            }
            return jsonify(retJson)

        #If i am here, then status_code == 200
        x = int(postedData["x"])
        y = int(postedData["y"])
        return x, y

    def JSONOutputMessage(self, function):
        retMap = {
            'Message': function,
            'Status Code': 200
        }
        return jsonify(retMap)

    


class Add(Resource):
    def post(self):
        #If I am here, then the resouce Add was requested using the method POST

        # Step 1: Get posted data:
        postedData = request.get_json()
        
        t = Tool()

        # Step 2: Add the posted data
        x, y = t.x_y_output(postedData, "add")
         
        ret = x + y
        return t.JSONOutputMessage(ret)

class Subtract(Resource):
    def post(self):
        # Step 1: Get posted data:
        postedData = request.get_json()
        
        t = Tool()

        # Step 2: Add the posted data
        x, y = t.x_y_output(postedData, "subtract")
         
        ret = x - y
        return t.JSONOutputMessage(ret)


class Multiply(Resource):
    def post(self):
        # Step 1: Get posted data:
        postedData = request.get_json()
        
        t = Tool()

        # Step 2: Add the posted data
        x, y = t.x_y_output(postedData, "multiply")
         
        ret = x * y
        return t.JSONOutputMessage(ret)

class Divide(Resource):
    def post(self):
        # Step 1: Get posted data:
        t = Tool()

        postedData = request.get_json()

        # Step 2: Add the posted data
        x, y = t.x_y_output(postedData, "divide")
         
        ret = (x* 1.0)/ y
        return t.JSONOutputMessage(ret)




# ###########################################################
# ##################### Run Application #####################
# ###########################################################

api.add_resource(Add, "/add")
api.add_resource(Subtract, "/sub")
api.add_resource(Multiply, "/mul")
api.add_resource(Divide, "/div")

@app.route('/')
def hello_world():        
    return "Hello World!"


if __name__=="__main__":
    app.run(debug=True)