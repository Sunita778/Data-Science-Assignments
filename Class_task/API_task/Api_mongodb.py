from flask import Flask, request, jsonify
import pymongo

app = Flask(__name__)

client = pymongo.MongoClient("mongodb+srv://sjkdh7:sjkdh8345@cluster0.t5kpe6z.mongodb.net/?retryWrites=true&w=majority")

database = client['task_mongo']
collection = database['task_collection']

@app.route("/insert/mongo", methods = ['POST'])
def insert():
    if request.method == 'POST':
        name = request.json['name']
        number = request.json['number']
        collection.insert_one({name : number})
        return jsonify(str("successfully inserted"))

@app.route("/update/mongo", methods = ['POST'])
def update():
    if request.method == 'POST':
        name = request.json['name']
        number = request.json['number']
        collection.update_one({name: number})
        return jsonify(str("successfully updated"))

@app.route("/delete/mongo", methods = ['POST'])
def delete():
    if request.method == 'POST':
        name = request.json['name']
        number = request.json['number']
        collection.delete_one({name: number})
        return jsonify(str("successfully deleted"))

@app.route("/fetch/mongo", methods = ['POST'])
def fetch():
    if request.method == 'POST':
        name = request.json['name']
        number = request.json['number']
        for i in collection.find():
            return jsonify(str(i))

if __name__ == '__main__':
    app.run()   # or for change port number app.run(port = 5001)
