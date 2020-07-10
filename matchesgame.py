import random


def usrinput():
  while bool('true'):
    usr = input('\npick a number from 1 to 3:')
    if usr in ["1","2","3"]:
      return int(usr)
    else:
      print('\nplease choose FROM 1,2 or 3')
      continue
    
def easymode():
  total = 21
  while total > 0:
    print('\nthe total matches left is:'+str(total))
    player = usrinput()
    if total - player <= 0:
      print('you lost to a randomly generated cpu LLL')
      break
    total = total - player
    cpu = random.randrange(1,4)
    if total - cpu <= 0:
      print('Winner winner chicken dinner')
      break
    total = total - cpu
    print('\nthe computers number of matches is: '+str(cpu))

def hardmode():
  total = 21 
  while bool('true'):
    print('\nthe total matches left is: '+str(total)) 
    usr = usrinput()
    if total - usr <= 0:
      print(' you lost to the cpu')
      break
    total = total - usr
    cpu = 4 - usr
    if total - cpu <= 0:
      print('Winner winner chicken dinner')
      break
    total = total - cpu
    print('\nthe computers number of matches is: '+str(cpu))
    
      
      
  
  
  



print('\nWelcome to the matches game, your goal is to NOT take the last match while starting at 21 and only being able to subtract 1,2 or 3 matches.\n')


while bool('true'):
  mode = input('what mode would you like to play? easy or hard: ')
  if mode == 'easy':
    easymode()
    break
  elif mode == 'hard':
    hardmode()
    break
  else:
    print('the mode you entered doesnt exist '+ mode)
    
    
    
  
  



  
  
  
    
   
  

