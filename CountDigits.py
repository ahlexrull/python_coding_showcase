# - Write a C program to count number of digits in a number.

#Note this is just for whole numbers, kindly use count_digits_f for float numbers

def count_digits(num):
  return len(str(num))

def count_digits_f(num):
  digits = "0123456789"
  count = 0

  for idx in range(len(str(num))):
      if str(num)[idx] in digits:
        count +=1

  return count
