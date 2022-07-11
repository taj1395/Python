doc = db.collection_name.find_one({"student_id": "1007"})
 
print(doc["student_id"])