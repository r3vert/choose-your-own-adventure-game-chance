import sys
from random import randint
encouter = randint(0, 9)
def my_function():
  if encouter == 0 or encouter == 1 or encouter == 2 or encouter == 3:
    print("nothing happened")
  elif encouter == 4 or encouter == 5 or encouter == 6 or encouter == 7 or encouter == 8:
    print("you encountered a monster")
  elif encouter == 9:
    print("You escaped")
input("press enter")
my_function()    







