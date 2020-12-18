import os
import sys
def restartprog():
  tryagain = input('do you want to try again')
  if tryagain == 'y' or tryagain == 'yes':
    os.execl(sys.executable, sys.executable, *sys.argv)
  else:
    sys.exit()