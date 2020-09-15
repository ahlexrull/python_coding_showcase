#- Given an array of length 10, reverse the array without using built-in reverse method. 

def reverse_arr(arr):
  rev_arr = []

  for ele in arr:
    rev_arr.insert(0, ele)
  
  return rev_arr

def reverse_arr_alt(arr):
  rev_arr = []
  
  i = -1
  while i >= len(arr) * -1:
    rev_arr.append(arr[i])
    i -= 1

  return rev_arr