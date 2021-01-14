from random import randint
from os import system, name
from time import sleep
from minorutil import restart
def lose():
  print("you lose! Better luck next time")
  restart.restartprog() 
def clearscr(): 
  #this will delete all previous text so it does not clutter the screen
  # for windows
  if name == 'nt':
    _ = system('cls')
  # for mac and linux(here, os.name is 'posix')
  else:
    _ = system('clear')
def encounter():
        sleep(0.5)
        clearscr()
        logic()
def logic():
  encouter = randint(0, 9)
  if encounter > 0 and encounter < 4:
    print("nothing happened")
  elif encounter > 3 and encounter < 9:
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
        print("In the hole you logic a large mutated rat. he eats you and you die in pain.")
      elif w == "dagger" or w == "d":
        print("You run into the bat stabbing it.")
        print("You live!")
      elif w == "sword" or w == "s":
        print("as you wave the sword around you suddenly fall into a hole")
        print("In the hole you logic a large mutated rat. he eats you and you die in pain.")
      else:
        print("invalid input")
        encounter()
    elif mo == 2:
      print("you encountered a skeleton!")    
      print("You have an bow, a dagger, and a sword")
      print("which will you choose?")
      w = input()
      clearscr()
      if w == "bow" or w == "b":
        print("The skeleton dodges the arrow! He stabs you ")
        print("In the hole you logic a large mutated rat. he eats you and you die in pain.")
        print("you died")
        lose()
      elif w == "dagger" or w == "d":
        print("You try and hit the skeleton but he hits you and he leaves you to bleed to death")
        print("You died")
        lose()
      elif w == "sword" or w == "s":
        print("as you wave the sword around you hit the ribs of it and it bursts into ")
        print("you win!")
      else:
        print("invalid input")
        encounter()
    else:
      print("3")
  elif encouter == 9:
    print("You escaped")
  else:
    print("Nice going! You found a bug. please report this")
if __name__ == "__main__":
   #Do something here
   encounter()



    







