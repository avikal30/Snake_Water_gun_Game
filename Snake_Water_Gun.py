#!/usr/bin/env python
# coding: utf-8

# In[8]:


# we are importing random module
# it has a randint function 
import random   



# In[16]:


def game(comp,you) :
    if comp == you :
        return None
    elif comp == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True
    elif comp == 'w' :
        if you == 'g':
            return False
        elif you == 's':
            return True
    elif comp == 'g':
        if you == 's':
            return False
        elif you == 'w':
            return True
    
    


# In[ ]:





# In[23]:


print('Comp turn: Snake(s) Water(w) or Gun(g) ?')
randNo = random.randint(1,3)
if(randNo == 1) :
    comp  = 's'
elif(randNo == 2 ) :
    comp = 'w' 
elif(randNo ==3) :
    comp   = 'g'

you = input("Your turn : Snake(s)  Water(w) or Gun(g) ?") 
randNo = random.randint(1,3)  
a = game(comp, you )

print(f'Computer chose {comp}')
print(f'You choose {a}' )
 
if a== None:
    print("The game is a tie") 
elif a:
    print("You win") 
else:
    print("You lost")


# In[ ]:





# In[ ]:




