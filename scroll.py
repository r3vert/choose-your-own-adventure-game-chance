import sys
from time import sleep
def scroll(str): 
  for letter in str:
    sys.stdout.write(letter)
    sys.stdout.flush()
    sleep(0.05) # change the number to make it faster/slower based on ur preference
scroll("is this working")