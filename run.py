from time import sleep
from encountersystem import clearscr
from encountersystem import encounter
#get persons name
def starttext():
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
    clearscr()
    print('The story shall start in a dark labyrinth')
    print('I hope you like it there, %s' % cname)
    print('The only way to go is forward.')
starttext()
encounter()    

  