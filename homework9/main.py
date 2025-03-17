# 1. დაწერეთ ფუნქცია, რომელიც პარამეტრად მიიღებს რიცხვს, თუ რამდენჯერ უნდა ჰკითხოს მომხმარებელს რიცხვი და საბოლოოდ დააჯამებს
#    ყველა შეყვანილ რიცხვს, თუ არგუმენტად არ გადაეცა არანაირი რიცხვი, მაშინ ფუნქციამ 5-ჯერ ჰკითხოს მომხმარებელს რიცხვის 
#    შეყვანა და დააჯამოს ეს 5 რიცხვი. დააბრუნეთ საბოლოო ჯამი

# def sum_numbers(times=5):
#     total = 0
#     for _ in range(times):
#         while True:
#             try:
#                 num = float(input("შეიყვანეთ რიცხვი: "))
#                 total += num
#                 break
#             except ValueError:
#                 print("გთხოვთ, შეიყვანოთ ვალიდური რიცხვი.")
#     return total

# # ფუნქციის გამოძახება
# result = sum_numbers()
# print("შეყვანილი რიცხვების ჯამი:", result)

# 2. დაწერეთ ფუნქცია რომელიც მიიღებს არგუმენტების განუსაზღვრელ რაოდენობას მთელი რიცხვების სახით და დააბრუნებს
#    ორ ლისტს, ერთ ლისტში იქნება გადაცმული არგუმენტებიდან კენტი რიცხვები ხოლო მეორე ლისტში ლუწი რიცხვები

# def separate_odd_even(*args):
#     odd_numbers = []
#     even_numbers = []

#     for num in args:
#         if num % 2 == 0:
#             even_numbers.append(num)
#         else:
#             odd_numbers.append(num)
    
#     return odd_numbers, even_numbers

# odd, even = separate_odd_even(1, 2, 3, 4, 5, 6)
# print("კენტი რიცხვები:", odd)
# print("ლუწი რიცხვები:", even)

# 3. დაწერეთ ფუნქცია, რომელსაც პარამეტრად გადაეცემა მომხმარებლის მიერ შეყვანილი წინადადება და ამ წინადადებაში დაითვლის სიტყვებს
#    და დიქტის სახით დააბრუნებს თუ რომელი სიტყვა რამდენჯერ არის, მაგ: "This is a test. This test is fun." --> დააბრუნებს დიქტის
#    შემდეგი სახით: {'this': 2, 'is': 2, 'a': 1, 'test': 2, 'fun': 1} უნდა იყოს case insensitive (ანუ დიდ და პატარა ასოებს არ უნდა
#    ჰქონდეს მნიშვნელობა!)

# def count_words(sentence):

#     words = sentence.lower().replace('.', '').replace(',', '').split()
    
#     # სიტყვების დათვლა და შედეგის დაბრუნება დიქტის სახით
#     word_count = {}
#     for word in words:
#         if word in word_count:
#             word_count[word] += 1
#         else:
#             word_count[word] = 1
            
#     return word_count
# sentence = "This is a test. This test is fun."
# print(count_words(sentence))

# 4. დაწერეთ რეკურსიული ფუნქცია, რომელსაც პარამეტრად გადაეცემა რიცხვი და დააბრუნებს 1-დან ამ რიცხვის ჩათვლით ყველა რიცხვის ჯამს

def sum_of_numbers(n):
    if n == 1:
        return 1
    else:
        return n + sum_of_numbers(n - 1)

print(sum_of_numbers(6))