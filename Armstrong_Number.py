given_number = float(input("Please enter number : "))
if given_number>0 and float(given_number)<=int(given_number) :
  given_number = int(given_number)
  sum_digits = 0
  digit = len(str(given_number))
  copy_number = given_number
  while copy_number > 0 :
    n_number = copy_number % 10
    sum_digits += n_number ** digit
    copy_number //= 10

  if given_number == sum_digits :
    print(given_number, "is an Arsmtrong number.")
  else:
    print(given_number, "is not an Armstrong number.")
else:
  print("Please enter valid number: ")
