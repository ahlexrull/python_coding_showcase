# - Write a C program to find first and last digit of a number.

def first_last_nums(num):
  print(f"first digit: {str(num)[0]} | last digit: {str(num)[-1]}")

def first_last_nums_arr(num):
  return(str(num)[0], str(num)[-1])