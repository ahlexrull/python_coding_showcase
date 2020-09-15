#- Given an array of length 10, reverse the array without using built-in reverse method. 

def reverse_arr(arr):
  rev_arr = []

  for ele in arr:
    rev_arr.insert(0, ele)
  
  return rev_arr