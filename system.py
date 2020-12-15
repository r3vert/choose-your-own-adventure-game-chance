import sys
from random import randint, random
from os import system, name
encouter = randint(0, 9)
def clearscr(): 
  #this will delete all previous text so it does not clutter the screen
  # for windows
  if name == 'nt':
    _ = system('cls')
  # for mac and linux(here, os.name is 'posix')
  else:
    _ = system('clear')
def encounter():
  if encouter == 0 or encouter == 1 or encouter == 2 or encouter == 3:
    print("nothing happened")
  elif encouter == 4 or encouter == 5 or encouter == 6 or encouter == 7 or encouter == 8:
    print("you encountered a monster")
    mo = randint(1, 3)
    if mo == 1:
      print("you encountered a bat!")    
      print("You have an bow, a dagger, and a sword")
      print("which will you choose?")
      w = input()
      clearscr()
      if w == "bow" or w == "b":
        print("the arrow misses! the bat hits you and you fall into a hole.")
        print("In the hole you encounter a large mutated rat. he eats you and you die in pain.")
        sys.exit()
      elif w == "dagger" or w == "d":
        print()
      elif w == "sword" or w == "s":
        print()
    elif mo == 2 or mo == 3:
      print("2 or 3")
  elif encouter == 9:
    print("You escaped")
encounter()



    







