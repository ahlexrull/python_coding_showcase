from OddNumbers import odd_num_arr

def sum_odd(num):
  sum = 0
  arr = odd_num_arr(num)

  for i in arr:
    sum += i

  return sum
