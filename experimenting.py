total = 0      
number = 1     

while number < 10:
    if number % 2 and total < 10:
        print(number)
    if number == 7:
        total += number - 3
    else:
        total += number
    number += 1

print(f"Mystery Answer: {total}")
