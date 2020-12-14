from time import sleep
from system import encounter
from os import system, name
import sys
from random import randint
goOn = True
one = 1
value = randint(1, 2)
#get persons name

pname = input('What is your name?\n')
print('Hi, %s.' % pname)
# sleep command waits for a amount of seconds for it to print the next line of text
sleep(0.9)

print('I am a bot with self conscience, %s ' % pname)
print('Im going to tell you a story')
#get caracters name
cname = input('What is your player name going to be.  \b')
print('I shall call you %s for now on' % cname)
print('Let the story begin')
sleep(0.9)

#this will delete all previous text so it does not clutter the screen

# for windows
if name == 'nt':
  _ = system('cls')

# for mac and linux(here, os.name is 'posix')
else:
  _ = system('clear')

print('The story shall start in a dark labyrinth')
print('I hope you like it there, %s' % cname)
print('where do you want to go east, west, north, or south.')
do = input()
if do == 'north':
    encounter()
elif do == 'south':
  encounter()
elif do == 'east':
  encounter()
  