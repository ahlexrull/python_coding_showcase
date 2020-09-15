# Input a 5 digits number from user, print its individual digits logically (without using loops, string indexing etc. )
import math

def five_digits():
  
  try:
    num = int(input("Please enter a number.\n"))

    print("")
    
    if len(str(num)) != 5:
      raise

    print( math.floor((num - (math.floor(num / 100000) * 100000)) /10000))

    print( math.floor((num - (math.floor(num / 10000) * 10000)) /1000))

    print( math.floor((num - (math.floor(num / 1000) * 1000)) /100))

    print( math.floor((num - (math.floor(num / 100) * 100)) /10))

    print( num - (math.floor(num / 10) * 10))

  except:
    print("Invalid length of number - Must be five digits")

      


  