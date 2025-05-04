# დაწერეთ ფუნქცია, რომელსაც პარამეტრად გადაეცემა რიცხვი და შეამოწმებს ეს რიცხვი არის თუ არა მარტივი

# შემდეგ ნაკადების გამოყენებით გაუშვით ეს ფუნქცია პარალელურად რომ შეამოწმოს შემდეგ ლისტში
# num_list = [17, 25, 74, 199, 101, 41, 39, 50, 20, 19, 51] ყველა რიცხვი და დააბრუნოს პასუხი

import concurrent.futures
import math

# მარტივი რიცხვის შემოწმების ფუნქცია
def is_prime(num):
    if num < 2:
        return (num, False)
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return (num, False)
    return (num, True)

num_list = [17, 25, 74, 199, 101, 41, 39, 50, 20, 19, 51]


results = {}
with concurrent.futures.ThreadPoolExecutor() as executor:
    futures = [executor.submit(is_prime, num) for num in num_list]
    for future in concurrent.futures.as_completed(futures):
        num, is_prime_flag = future.result()
        results[num] = is_prime_flag

# შედეგების დაბეჭდვა
for num in sorted(results):
    print(f"{num} is {'prime' if results[num] else 'not prime'}")