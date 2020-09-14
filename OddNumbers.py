# Write a C program to print all odd number between 1 to 100.

def odd_num(num):
  i = 0
  while i <= num:
    if i % 2 != 0:
      print(i)
    i += 1

#this can be used in general and then a loop just print out the returned arr so you dont need the function above
def even_num_arr(num):
  arr = []
  i = 1
  while i <= num:
    if i % 2 != 0:
      arr.append(i)
    i += 2
  return arr
