# 1 დავალება

# import csv

# def collect_and_save_data(entries: int, filename: str = "users_data.csv"):
#     fieldnames = ["ID", "first_name", "last_name", "age"]
    
#     with open(filename, mode='w', newline='', encoding='utf-8') as file:
#         writer = csv.DictWriter(file, fieldnames=fieldnames)
#         writer.writeheader()
        
#         for i in range(1, entries + 1):
#             first_name = input(f"[{i}] Enter first name: ")
#             last_name = input(f"[{i}] Enter last name: ")
            
#             while True:
#                 try:
#                     age = int(input(f"[{i}] Enter age: "))
#                     break
#                 except ValueError:
#                     print("Invalid input! Please enter a valid integer for age.")
            
#             writer.writerow({"ID": i, "first_name": first_name, "last_name": last_name, "age": age})
    
#     print(f"Data successfully saved to {filename}")

# # ფუნქციის გამოძახება
# try:
#     num_entries = int(input("Enter the number of entries: "))
#     collect_and_save_data(num_entries)
# except ValueError:
#     print("Please enter a valid integer for the number of entries!")

# 2 დავალება

import csv

# ფაილების სახელები
input_file = "students.csv"
failed_file = "failed_students.csv"
passed_file = "passed_students.csv"

# ფაილის წაკითხვა
with open(input_file, mode="r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    students = list(reader)

# სტუდენტების დაყოფა ქულების მიხედვით
failed_students = [student for student in students if int(student["Grade"]) < 50]
passed_students = [student for student in students if int(student["Grade"]) > 50]

# ჩაწერა ახალ ფაილებში
def write_to_csv(filename, data):
    if data:
        with open(filename, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)

# ახალი ფაილების შექმნა
write_to_csv(failed_file, failed_students)
write_to_csv(passed_file, passed_students)

print("ფაილები შეიქმნა წარმატებით!")

