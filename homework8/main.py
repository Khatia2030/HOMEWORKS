# 1. დაწერეთ ფუნქცია, რომელიც პარამეტრად მიიღებს მომხმარებლის მიერ შეყვანილ ტექსტს და ამ ტექსტში დათვლის რამდენი სიმბოლო იყო მაღალ რეგისტრში
#    შეყვანილი და ასევე ამ ტექსტს გადააქცევს uppercase-ად ანუ მაღალ რეგისტრში დააბრუნებს, მაგალითად, მომხმარებელმა თუ შეიყვანა ტექსტი
#    Hello woRld, ფუნქციამ უნდა დააბრუნოს რომ 2 დიდი ამ ტექსტში და ეს ტექსტი აქციოს HELLO WORLD-ად.

# def text(text):
#     uppercase_count = sum(1 for char in text if char.isupper())
#     uppercase_text = text.upper()
#     return uppercase_count , uppercase_text

# user_input=input("შეიყვანეთ ტექსტი: ")
# count, transformed_text = text(user_input)
# print(f"დიდი ასოების რაოდენობა: {count}")
# print(f"uppercase ტექსტი: {transformed_text}")

# 2. დაწერეთ ფუნქცია, რომელიც პარამეტრად მიიღებს ე.წ. camel case ცვლადებს და დააბრუნებს snake case სახით, ანუ თუ გადავცემთ ცვლადს
#    firstName დააბრუნებს first_name, name დააბრუნებს ისევ name, preferredFirstName დააბრუნებს preferred_first_name, lastName დააბრუნებს
#    last_name და ასე შემდეგ.

import re

def process_text(text):
    uppercase_count = sum(1 for char in text if char.isupper())  
    uppercase_text = text.upper()  
    return uppercase_count, uppercase_text

def camel_to_snake(camel_str):
    snake_str = re.sub(r'([a-z])([A-Z])', r'\1_\2', camel_str).lower()
    return snake_str


user_input = input("შეიყვანეთ camelCase ცვლადი: ")
snake_case = camel_to_snake(user_input)
print(f"snake_case სახელი: {snake_case}")

user_input = input("შეიყვანეთ ტექსტი: ")
count, transformed_text = process_text(user_input)
print(f"დიდი ასოების რაოდენობა: {count}")
print(f"uppercase ტექსტი: {transformed_text}")