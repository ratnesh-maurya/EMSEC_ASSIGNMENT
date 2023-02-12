import csv
import io
import pandas as pd
from flask import Flask, jsonify, request, redirect, Response
from flask.helpers import url_for
from flask_pymongo import PyMongo
from flask_cors import CORS, cross_origin
# Initialize Flask Application
app = Flask(__name__)
cors = CORS(app)
# Connect to the MongoDB database using the PyMongo library
app.config['MONGO_URI'] = 'mongodb+srv://RATNESH:Aith@RatneshApi.isrqwuj.mongodb.net/RatneshApi'
app.config['CORS_Headers'] = 'Content-Type'
mongo = PyMongo(app)

# see all data

# Route for retrieving all data from the 'user' collection in the MongoDB database
@app.route('/', methods=['GET'])
@app.route('/', methods = ['GET'])
def retrieveAll():
    holder = list()
    currentCollection = mongo.db.user
    for i in currentCollection.find():
        holder.append({'name':i['name'], 'password' : i['password'], 'role' : i['role']})
    return jsonify(holder)

# see one data

@app.route('/<name>', methods = ['GET'])
@cross_origin()
def retrieveFromName(name):
    currentCollection = mongo.db.user
    data = currentCollection.find_one({"name" : name})
        # Return the retrieved data as a JSON object
    return jsonify({'name' : data['name'], 'password' : data['password'], 'role' : data['role']})

# add data

@app.route('/postData', methods = ['POST'])
def postData():
    currentCollection = mongo.db.user
    name = request.json['name']
    password = request.json['password']
    role = request.json['role']
    currentCollection.insert({'name' : name, 'password' : password, 'role' : role})
    return jsonify({'name' : name, 'password' : password, 'role' : role})

# delete data

@app.route('/deleteData/<name>', methods = ['DELETE'])
def deleteData(name):
    currentCollection = mongo.db.user
    currentCollection.delete_one({'name' : name})
    return redirect(url_for('retrieveAll'))

# update data

@app.route('/update/<name>', methods = ['PUT'])
def updateData(name):
    currentCollection = mongo.db.user
    updatedName = request.json['name']
    currentCollection.update_one({'name':name}, {"$set" : {'name' : updatedName}})
    return redirect(url_for('retrieveAll'))

# Pagination

@app.route("/api/users", methods=["GET"])
def get_user_list_api():
    page_number = int(request.args.get("page", 1))
    users = get_user_list(page_number)
    return {"users": users}, 200

# Convert to CSV

@app.route("/api/users/export", methods=["GET"])
def export_users_api():
    users = list(collection.find())
    df = pd.DataFrame(users)
    csv = df.to_csv(index=False)
    return Response(
        csv,
        mimetype="text/csv",
        headers={"Content-disposition": "attachment; filename=users.csv"}
    )

if __name__ == '__main__':
    app.run(debug = True)