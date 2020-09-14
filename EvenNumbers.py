# Write a C program to print all even numbers between 1 to 100. - using while loop

def even_num(num):
  i = 1
  while i < num:
    if i % 2 == 0 :
      print(i)
    i += 1