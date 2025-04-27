# pymongo-ს გამოყენებით დაუკავშირდით MongoDB-ს და გააკეთეთ შემდეგი ოპერაციები:


from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
# print(client.list_database_names())
db = client["PP-25"]
# კოლექციაში შეიტანეთ მინიმუმ 10 მონაცემი, მონაცემები უნდა იყოს მსგავი სახის:
# {
#   "name": "John Doe",
#   "age": 20,
#   "grade": "B",
#   "courses": ["Math", "Science"],
#   "address": {
#     "city": "New York",
#     "zipcode": "10001"
#   },
#   "attendance": 85
# }

students_collection = db["students"]
students = [
    {
        "name": "John Doe",
        "age": 20,
        "grade": "B",
        "courses": ["Math", "Science"],
        "address": {"city": "New York", "zipcode": "10001"},
        "attendance": 85
    },
    {
        "name": "Jane Smith",
        "age": 22,
        "grade": "A",
        "courses": ["English", "History"],
        "address": {"city": "Los Angeles", "zipcode": "90001"},
        "attendance": 90
    },
    {
        "name": "Emily Johnson",
        "age": 19,
        "grade": "C",
        "courses": ["Biology", "Chemistry"],
        "address": {"city": "Chicago", "zipcode": "60601"},
        "attendance": 80
    },
    {
        "name": "Michael Brown",
        "age": 21,
        "grade": "B",
        "courses": ["Physics", "Math"],
        "address": {"city": "Houston", "zipcode": "77001"},
        "attendance": 88
    },
    {
        "name": "Chris Davis",
        "age": 23,
        "grade": "A",
        "courses": ["Economics", "Math"],
        "address": {"city": "Phoenix", "zipcode": "85001"},
        "attendance": 95
    },
    {
        "name": "Patricia Wilson",
        "age": 20,
        "grade": "B",
        "courses": ["Art", "Design"],
        "address": {"city": "Philadelphia", "zipcode": "19101"},
        "attendance": 87
    },
    {
        "name": "Robert Martinez",
        "age": 24,
        "grade": "C",
        "courses": ["Programming", "Data Science"],
        "address": {"city": "San Antonio", "zipcode": "78201"},
        "attendance": 75
    },
    {
        "name": "Linda Anderson",
        "age": 22,
        "grade": "B",
        "courses": ["Law", "Politics"],
        "address": {"city": "San Diego", "zipcode": "92101"},
        "attendance": 82
    },
    {
        "name": "David Thomas",
        "age": 21,
        "grade": "A",
        "courses": ["Math", "Computer Science"],
        "address": {"city": "Dallas", "zipcode": "75201"},
        "attendance": 93
    },
    {
        "name": "Barbara Jackson",
        "age": 23,
        "grade": "B",
        "courses": ["Marketing", "Management"],
        "address": {"city": "San Jose", "zipcode": "95101"},
        "attendance": 89
    }
]
# students_collection.insert_many(students)
# print("მონაცემები წარმატებით დაემატა!")

# იპოვეთ ყველა სტუდენტი რომელიც ცხოვრობს New York-ში
# students_in_new_york = students_collection.find({"address.city": "New York"})
# for student in students_in_new_york:
#     print(student)

# იპოვეთ ყველა სტუდენტი რომლის ასაკიც მეტია 18-ზე
# students_older_than_18 = students_collection.find({"age": {"$gt": 18}})
# for student in students_older_than_18:
#     print(student)

# იპოვეთ ყველა სტუდენტი რომელსაც აქვს კურსი Math
# students_with_math = students_collection.find({"courses": "Math"})
# for student in students_with_math:
#     print(student)

# დაითვალეთ რამდენ სტუდენტს აქვს A შეფასება
# students_with_A = students_collection.find({"grade": "A"})
# count = len(list(students_with_A))
# print(f"შეფასება 'A' ჰქონდათ {count} სტუდენტს.")

# იპოვეთ ყველა სტუდენტი რომელიც ცხოვრობს Los Angeles-ში და attendance >= 90
# students_in_los_angeles = students_collection.find({
#     "address.city": "Los Angeles",
#     "attendance": {"$gte": 90}
# })
# for student in students_in_los_angeles:
#     print(student)

# დააფდეითეთ John Doe-ს შეფასება A შეფასებით
# result = students_collection.update_one(
#     {"name": "John Doe"},  
#     {"$set": {"grade": "A"}}  
# )
# if result.modified_count > 0:
#     print("John Doe-ს შეფასება წარმატებით განახლდა!")
# else:
#     print("შეფასების განახლება არ მოხდა.")

# დაამატეთ ახალი ველი ყველა სტუდენტისთვის "graduated": false
# result = students_collection.update_many(
#     {},  
#     {"$set": {"graduated": False}}  
# )
# print(f"განახლდა {result.modified_count} სტუდენტი(ები).")

# სტუდენტები, რომლებსაც აქვთ შეფასება B, დაუმატეთ კურსებში "English" კურსი
# result = students_collection.update_many(
#     {"grade": "B"},  
#     {"$addToSet": {"courses": "English"}}  
# )
# print(f"კურსები განახლდა {result.modified_count} სტუდენტ(ი)ში.")

# წაშალეთ სტუდენტი, რომლის სახელია "Alice Smith"
# result = students_collection.delete_one({"name": "Alice Smith"})
# if result.deleted_count > 0:
#     print("Alice Smith წარმატებით წაიშალა.")
# else:
#     print("Alice Smith არ მოიძებნა.")

# წაშალეთ ყველა სტუდენტი, რომლის დასწრების მაჩვენებელია 60-ზე ნაკლები
# result = students_collection.delete_many({"attendance": {"$lt": 60}})
# print(f"წაიშალა {result.deleted_count} სტუდენტი(ები), რომელთა დასწრების მაჩვენებელიც იყო 60-ზე ნაკლები.")
