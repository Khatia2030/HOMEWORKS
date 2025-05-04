import json
import random
from faker import Faker

fake = Faker('ka_GE')  # ქართული ლოკალი

# 1. სტუდენტების სიის გენერაცია
students = []
for _ in range(100):
    student = {
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "email": fake.email(),
        "age": random.randint(18, 70),
        "is_active": random.choice([True, False])
    }
    students.append(student)

# 2. სტუდენტების ჩაწერა ფაილში (students.json)
with open("students.json", "w", encoding="utf-8") as file:
    json.dump(students, file, indent=4, ensure_ascii=False)

# 3. სტუდენტების წაკითხვა ფაილიდან
with open("students.json", "r", encoding="utf-8") as file:
    data = json.load(file)

# 4. გაფილტვრა აქტიური სტუდენტების
active_students = [student for student in data if student["is_active"]]

# 5. აქტიური სტუდენტების ჩაწერა ახალ ფაილში (active_students.json)
with open("active_students.json", "w", encoding="utf-8") as file:
    json.dump(active_students, file, indent=4, ensure_ascii=False)

# 6. მაგალითების დაბეჭდვა კონსოლში
print("\n(students.json):")
for student in data[:5]:  # პირველი 5 სტუდენტი
    print(student)

print("\n  (active_students.json):")
for student in active_students[:5]:  # პირველი 5 აქტიური სტუდენტი
    print(student)