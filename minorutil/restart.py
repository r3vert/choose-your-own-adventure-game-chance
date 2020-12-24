from os import name,system
import sys
def restartprog():
  tryagain = input('do you want to try again')
  if tryagain == 'y' or tryagain == 'yes':
  # for windows
    if name == 'nt':
      system("python -3")
    # for mac and linux(here, os.name is 'posix')
    else:
      system("python3 run.py")
  else:
    sys.exit()