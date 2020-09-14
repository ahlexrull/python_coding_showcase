from EvenNumbers import even_num_arr

def sum_even(number):
  arr = even_num_arr(number) #grabs the function from the Even Numbers module
  sum = 0

  for num in arr:
    sum += num
  
  return sum
