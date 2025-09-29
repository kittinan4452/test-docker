from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)

# Setting up MongoDB client and database
client = MongoClient("mongodb://mymongo:27017")
db = client["mydb"]
collection = db["users"]  # Table equivalent in MongoDB

@app.route('/')
def home():
    return '<h1>Hello Application</h1>'

@app.route('/data')
def get_data():
    users = collection.find()  # Find all users
    user_data = []
    
    for user in users:
        user_data.append(f"name: {user['name']} , age: {user['age']} years")
    
    return "<br>".join(user_data)

def init_database():
    # Check if there are no documents in the collection
    if collection.count_documents({}) == 0:
        collection.insert_one({"name": 'tii', "age": 24})
        print("Document saved.")

if __name__ == '__main__':
    init_database()
    app.run(host='0.0.0.0', port=5000)
