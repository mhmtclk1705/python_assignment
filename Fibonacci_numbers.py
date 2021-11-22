# Task : Create a list consisting of Fibonacci numbers from 1 to 55 using control flow statements.

# The desired output is like :

# fibonacci →  [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
number_1 = 1
number_2 = 1
f_list = []
count = 0
f_numbers = 0
while number_1 <= 55:
  f_list.append(number_1)
  f_numbers = number_1 + number_2
  number_1 = number_2
  number_2 = f_numbers
  

print(f_list)


