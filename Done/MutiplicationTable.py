# Write a C program to print multiplication table of any number.

from NaturalNumbers import natural_arr

def mult_table(num):
  arr_table = [] #the main 2d array that will hold the multiplication table

  for idx1 in range(num+1): #iterates through each row
    if idx1 == 0: #when on the first row
      arr_table.append(natural_arr(num)) #print out the range of natural numbers

    else:
      idx2 = 0
      arr = []

      while idx2 <= num: #iterates through the columns

        if idx2 == 0: #initializes the first value in the the row
          arr.append(idx1)

        else: #multiplies the first value with the number at index of idx2 in the arr_tables first row and appends it to the array
          res = arr[0] * arr_table[0][idx2]
          arr.append(res)
        
        idx2 += 1

      arr_table.append(arr) #appends the entire row to the main arr_table

  return arr_table

def mult_table_f(num): #used to call the mult_table in table format
    arr = mult_table(num)
    for row in arr:
      print(f"{row} \n")

