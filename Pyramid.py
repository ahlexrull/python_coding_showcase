#- Input a number, have your program draw a pyramid on screen of that much levels.
import math

def pyramid(num):
  for idx in range((num*2)+1):
    if idx != 0 and idx % 2 != 0:
      print(" "*math.ceil((num * 2 - idx)/2) + "*"*idx)