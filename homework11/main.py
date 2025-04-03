#  1. დაწერეთ პროგრამა, რომელიც მომხმარებელს უსასრულოდ შეეკითხება ჯერ სახელს, შემდეგ გვარს და რაიმე ფაილში ჩაწერს 
#     სახელს და გვარს ერთ ხაზზე თავისი ნუმერაციით, ყველა ახალი სახელი და გვარი უნდა იყოს ახალ ხაზზე ჩაწერილი
# file_name = "names.txt"
# def write_to_file(counter, first_name, last_name):
#     with open(file_name, "a") as file:
#         file.write(f"{counter}. {first_name} {last_name}\n")
# counter = 1
# while True:
#     first_name = input("გთხოვთ, შეიყვანოთ სახელი (ან დაწერეთ 'stop' პროგრამის გასაჩერებლად): ")
    
#     # თუ მომხმარებელი ჩაწერს "stop", პროგრამა შეწყვეტს მუშაობას
#     if first_name.lower() == "stop":
#         print("პროგრამა შეჩერდა.")
#         break
    
#     last_name = input("გთხოვთ, შეიყვანოთ გვარი: ")
    
#     write_to_file(counter, first_name, last_name)
#     print(f"{counter}. {first_name} {last_name} წარმატებით ჩაიწერა ფაილში.")
    
#     counter += 1

# 2 დავალება
file_name = "persons.txt"
input_file = "persons.txt"
under_50_file = "under_50.txt"
over_50_file = "over_50.txt"
# მონაცემების წაკითხვა "persons.txt"-დან
def read_persons(file_name):
    with open(file_name, "r") as file:
        return file.readlines()

# პიროვნებების გაყოფა ასაკის მიხედვით
def split_by_age(persons):
    under_50 = []
    over_50 = []
    
    for person in persons:
        # პიროვნების მონაცემების გაყოფა
        name, age, city = person.strip().split(", ")
        age = int(age)
        
        # ასაკის მიხედვით გაყოფა
        if age < 50:
            under_50.append(f"{name}, {age}, {city}")
        else:
            over_50.append(f"{name}, {age}, {city}")
    
    return under_50, over_50
# მონაცემების ჩაწერა ახალ ფაილში
def write_to_file(file_name, data):
    with open(file_name, "w") as file:
        for person in data:
            file.write(f"{person}\n")

# მთავარი პროგრამა
persons = read_persons(input_file)
under_50, over_50 = split_by_age(persons)

# ფაილების შექმნა და მონაცემების ჩაწერა
write_to_file(under_50_file, under_50)
write_to_file(over_50_file, over_50)

print(f"პიროვნებები, რომელთა ასაკია 50 წლამდე, ჩაიწერა ფაილში '{under_50_file}'.")
print(f"პიროვნებები, რომელთა ასაკია 50-ზე მეტი, ჩაიწერა ფაილში '{over_50_file}'.")