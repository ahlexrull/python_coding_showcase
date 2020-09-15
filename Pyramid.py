#- Input a number, have your program draw a pyramid on screen of that much levels.

def pyramid(num):
  for idx in range(num+1):
    if idx != 0:
      print(" "*(num - idx) + "*"*idx)