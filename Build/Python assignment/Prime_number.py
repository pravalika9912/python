
num =int(input("Enter a number:"))
for i in range (2, num):
    if (num% i) == 0 and num>1:
      print ("The provided number is not a prime number")
    else:
      print ("The number is a prime number")
  
