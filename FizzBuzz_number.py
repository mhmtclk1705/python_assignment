list = []
for i in range(1,101):
  if i % 15 == 0:
    i = "FizzBuzz"
    list.append(i)
  elif i % 3 == 0:
    i = "Fizz"
    list.append(i)
  elif i % 5 == 0:
    i = "Buzz"
    list.append(i)
  else :
    list.append(i)
print(list)