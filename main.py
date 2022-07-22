print("Wellcome to Oguz's leap year checker/calculator")
year = int(input("Which year do you want to check? \n "))

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("leap year")
    else:
      print("not a leap year")
  else:
    print("leap year")
else:
  print("not a leap year")