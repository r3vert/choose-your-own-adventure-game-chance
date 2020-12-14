import sys
from random import randint, random
encouter = randint(0, 9)
def encounter():
  if encouter == 0 or encouter == 1 or encouter == 2 or encouter == 3:
    print("nothing happened")
  elif encouter == 4 or encouter == 5 or encouter == 6 or encouter == 7 or encouter == 8:
    print("you encountered a monster")
    mo = randint(1, 3)
    if mo == 1:
      print("you encountered a bat!")    
      print("You have an bow, a dagger, and a long sword")
      w = input("which will you choose")
      if w == "bow":
        print("the arrow misses! the bat hits you and you fall into a hole.")
        print("In the hole you encounter a large mutated rat. he eats you and you die in pain.")
        input()
        sys.exit()
  elif encouter == 9:
    print("You escaped")

    







