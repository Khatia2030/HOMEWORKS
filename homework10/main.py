# 1. გამოიყენეთ lambda ფუნქცია sorted() ფუნქციაში, იმისათვის რომ დაასორტიროს მოცემული ლისტი:
#    [(1, 3), (4, 2), (2, 5)] - მასში არსებული ელემენტების მეორე ელემენტის მიხედვით
# my_list = [(1, 3), (4, 2), (2, 5)]
# sorted_list = sorted(my_list, key=lambda x: x[1])
# print(sorted_list)
# 2. დაწერეთ ფუნქცია, რომელიც მომხმარებელს შეაყვანინებს ორ რიცხვს და პირველ რიცხვს გაყოფს მეორე რიცხვზე და დააბრუნებს შედეგს, 
# დაიჭირეთ ორი ერორი: ის რომ მომხმარებელმა ინტეჯერები შეიყვანოს და ნულზე რომ არ შეიძლება გაყოფა, თითოეული ერორისთვის გამოუტანეთ 
# შესაბამისი შეტყობინება. (ორივე ერორი უნდა იყოს შესაბამისი ერორებით დაჭერილი, არ გამოიყენოთ ზოგადი იქსეფშენი)
# def divide_numbers():
#     try:
#         num1 = int(input("შეიყვანეთ პირველი რიცხვი: "))
#         num2 = int(input("შეიყვანეთ მეორე რიცხვი: "))
        
#         # შესამოწმებელი გაყოფა
#         result = num1 / num2
#         print(f"გაყოფის შედეგი: {result}")
    
#     except ValueError:
#         # შეცდომა, თუ მომხმარებელი არ შეიყვანს ინტეჯერებს
#         print("შეიყვანეთ მხოლოდ რიცხვები.")
    
#     except ZeroDivisionError:
#         # შეცდომა, თუ მომხმარებელი 0-ით ცდილობს გაყოფას
#         print("გაყოფა ნულზე არ შეიძლება.")

# divide_numbers()
# 3. მოცემულია პროდუქტების ლისტი:

#    products = [
#     {"name": "Laptop", "price": 1200},
#     {"name": "Mouse", "price": 15},
#     {"name": "Keyboard", "price": 25},
#     {"name": "Monitor", "price": 150},
#     {"name": "Power", "price": 100},
#     {"name": "Pad", "price": 10},
# ]

# filter() ფუნქციის გამოყენებით გაფილტრეთ და გამოიტანეთ პროდუქტები, რომლის ფასი ნაკლებია 100-ზე;
# map() ფუნქციის გამოყენებით გამოიტანეთ ყველა პროდუქტის სახელი და ფასი
# sorted() ფუნქციის გამოყენებით დაასორტირეთ პროდუქტების სია ფასის მიხედვით
# reduce() ფუნქციის გამოყენებით გამოიტანეთ ყველა პროდუქტის ფასების ჯამი

from functools import reduce
products = [
    {"name": "Laptop", "price": 1200},
    {"name": "Mouse", "price": 15},
    {"name": "Keyboard", "price": 25},
    {"name": "Monitor", "price": 150},
    {"name": "Power", "price": 100},
    {"name": "Pad", "price": 10},
]
# filter() - პროდუქტები, რომლის ფასი ნაკლებია 100-ზე
filtered_products = list(filter(lambda x: x["price"] < 100, products))
print("Filtered products (price < 100):", filtered_products)

# map() - ყველა პროდუქტის სახელი და ფასი
mapped_products = list(map(lambda x: f'{x["name"]}: ${x["price"]}', products))
print("Mapped products (name and price):", mapped_products)

# sorted() - პროდუქტის სიის დამახსოვრება ფასის მიხედვით
sorted_products = sorted(products, key=lambda x: x["price"])
print("Sorted products (by price):", sorted_products)

# reduce() - ყველა პროდუქტის ფასების ჯამი
total_price = reduce(lambda x, y: x + y["price"], products, 0)
print("Total price of all products:", total_price)