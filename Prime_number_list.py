number = int(input("Please enter limit number for prime number list: "))
list = []
for i in range(2,number+1) :
  for j in range(2,i) :
    if i % j == 0 :
      break
  else:
    list.append(i)


print(list)
