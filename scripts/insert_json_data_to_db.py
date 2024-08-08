import json
from pymongo import MongoClient, ASCENDING

def insert_data_to_db():
    try:
        # Load the data from the JSON file
        with open('../courses.json', 'r') as file:
            courses = json.load(file)

        # Connect to the MongoDB server
        client = MongoClient('mongodb://localhost:27017/')
        db = client['course_database']
        collection = db['courses']

        # Create indices
        collection.create_index([("name", ASCENDING)])
        collection.create_index([("date", ASCENDING)])
        collection.create_index([("domain", ASCENDING)])

        # Insert data
        for course in courses:
            collection.insert_one(course)

        print("Data inserted to MongoDB successfully.")
        return True

    except Exception as e:
        print(e)
        return False
    
insert_data_to_db()