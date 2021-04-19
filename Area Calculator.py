#You are painting a wall. The instructions on the paint can says that 1 can of paint can cover 5 square meters of wall. Given a random height and width of wall, calculate how many cans of paint you'll need to buy.

import math
height = int(input("Enter the wall height: "))
widht = int(input("Enter the width of wall: "))
coverage = 5
def paint_calc(test_h = height,test_w = widht):
  area = test_h * test_w
  number = math.ceil(area / coverage)
  print(f"You'll need {number} cans of paint")
paint_calc()