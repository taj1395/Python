from pymongo import MongoClient
conn = MongoClient("localhost", 27017)
db = conn["mydb"]
collection = db.students
cursor = collection.find()
for record in cursor:
	print(record)
result = collection.delete_one({"student_id":1007},
{
	"$set":
	{
	"last_name":"Jones"
}
}
)

cursor = collection.find()

for record in cursor:

	print(record)
