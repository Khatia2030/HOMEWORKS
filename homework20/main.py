import json
import os

def add_persons_to_json(n):
    filename = 'persons.json'

    if os.path.exists(filename):
        with open(filename, 'r') as file:
            try:
                persons = json.load(file)
            except json.JSONDecodeError:
                persons = []
    else:
        persons = []

    last_id = persons[-1]['id'] if persons else 0

    for _ in range(n):
        name = input("Enter your name: ")
        while True:
            age_input = input("Enter your age: ")
            if age_input.isdigit():
                age = int(age_input)
                break
            else:
                print("Age must be a number.")
        
        new_person = {
            "id": last_id + 1,
            "name": name,
            "age": age
        }
        persons.append(new_person)
        last_id += 1

    with open(filename, 'w') as file:
        json.dump(persons, file, indent=4)
    
    print(f"{n} person(s) added to {filename} successfully.")


add_persons_to_json(2)
