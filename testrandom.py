from random import randint
one = 1
value = randint(1, 2)
print(value)
do = input()
if do == 'north':
  if value == one:
    print("you died")
  else:
    print("you survived")