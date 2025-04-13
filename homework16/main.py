# 1. დაწერეთ ტრანზაქციის ფუნქცია, რომელსაც გადაეცემა ატრიბუტად ბალანსი და გადასახდელი თანხა, დაუწერეთ დეკორატორი, 
# რომელიც საკომისიოს ჩამოაჭრის 1 ლარს და თუ საკმარისი თანხა არ იქნება ანგარიშზე დაუბრუნეთ შეცდომის ტექსტი

# # დეკორატორი, რომელიც საკომისიოს აკლებს თანხიდან
# def commission_decorator(func):
#     def wrapper(balance, amount):
#         commission = 1
#         total_amount = amount + commission
#         if balance < total_amount:
#             return "შეცდომა: ბალანსი არასაკმარისია ტრანზაქციისთვის (თანხა + საკომისიო)"
#         return func(balance, amount, commission)
#     return wrapper

# # ტრანზაქციის ფუნქცია
# @commission_decorator
# def make_transaction(balance, amount, commission):
#     new_balance = balance - amount - commission
#     return f"ტრანზაქცია წარმატებით შესრულდა! ახალი ბალანსია: {new_balance} ლარი"
# print(make_transaction(50, 20))   # წარმატებული ტრანზაქცია
# print(make_transaction(20, 20))   # შეცდომა — არასაკმარისი ბალანსი

# 2. შექმენით მეტაკლასი, რომელიც სხვა კლასზე გამოყენების შემთხვევაში შეამოწმებს ამ კლასის მეთოდის სახელებს,
#    შემდეგი სახით: თუ მეთოდი იწყება _ ეს მეთოდი ვალიდური იქნება, თუ არ იწყება _, მაშინ აღზევდეს 
#    ValueError. მაგ: _test() - ეს მეთოდი იქნება ვალიდური, test() - ეს მეთოდი არ იქნება ვალიდური
#    და გამოიწვევს ValueError-ს. გაითვალისწინეთ რომ მეტაკლასმა უნდა შეამოწმოს მხოლოდ მეთოდები და არა ატრიბუტები!

class MethodNameValidatorMeta(type):
    def __new__(cls, name, bases, class_dict):
        for attr_name, attr_value in class_dict.items():
            # ვამოწმებთ არის თუ არა ატრიბუტი ფუნქცია (მეთოდი)
            if callable(attr_value) and not attr_name.startswith("_"):
                raise ValueError(f"მეთოდი '{attr_name}' არ იწყება '_' სიმბოლოთი")
        return super().__new__(cls, name, bases, class_dict)
    
    # სწორად გამოცხადებული კლასი
class ValidClass(metaclass=MethodNameValidatorMeta):
    def _valid_method(self):
        pass

    def __str__(self):  # მაგ: მაგიური მეთოდებიც ვალიდურად ჩაითვლება
        return "Valid"
# არასწორად გამოცხადებული კლასი — გამოიწვევს შეცდომას
class InvalidClass(metaclass=MethodNameValidatorMeta):
    def invalid_method(self):  # არ იწყება _
        pass
