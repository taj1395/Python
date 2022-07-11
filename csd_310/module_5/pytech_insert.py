from pymongo import MongoClient

# Create a pymongo client
client = MongoClient("localhost", 27017)

# Get the database instance
db = client["mydb"]

# db collection
pytech = db["PyTech"]

# insert 3 students
records = [
    {
        "student_id": "1007",
        "first_name": "Fred",
        "last_name": "Jones"
    },
    {
        "student_id": "1008",
        "first_name": "Jane",
        "last_name": "Doe"
    },
    {
        "student_id": "1009",
        "first_name": "Tim",
        "last_name": "Barnes"
    }
]

for record in records:
    new_student_Id = pytech.insert_one(record).inserted_id
    print(new_student_Id)
    
# display all documents in the collection
docs = pytech.find()

for doc in docs:
    print(doc)
    
# display a single document by student_id
print(pytech.find_one({"student_id": "1008"}))