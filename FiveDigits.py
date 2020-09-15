# Input a 5 digits number from user, print its individual digits logically (without using loops, string indexing etc. )

def five_digits():
  
  try:
    str_num = str(input("Please enter a number.\n"))

    if len(str_num) != 5:
      raise 
    else:
      print(f" {str_num[0]} |  {str_num[1]} |  {str_num[2]} |  {str_num[3]} |  {str_num[4]} " )
      
  except:
    print("Invalid length, please use a number with 5 digits ")

  