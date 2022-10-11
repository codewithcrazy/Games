import random

def tie():
    pass

def game(comp,player):
    if(player == comp):
        return None
    elif(comp == 's'):
        if(player == 'w'):
            return False
        elif(player == 'g'):
            return True
    elif(comp == 'w'):
        if(player == 's'):
            return True
        elif(player == 'g'):
            return False
    elif(comp == 'g'):
        if(player == 's'):
            return False
        elif(player == 'w'):
            return True
        


print("Computer Turn : Snake(s) Water(w) or Gun(g) ?")
randnum=random.randint(1,3)
if randnum == 1:
    comp = 's'
elif randnum == 2:
    comp = 'w'
elif randnum ==3 :
    comp = 'g'

player=input("Your's Turn : Snake(s) Water(w) or Gun(g) ? -  ").lower()
while(not (player == 's' or player == 'w' or player == 'g')):
    player=input("Your's Turn : Snake(s) Water(w) or Gun(g) ? -  ").lower()
score = game(comp,player)
print(f"Computer choose {comp}")
print(f"You choose {player}")
if score == None:
    print("Game is Tie")
elif score == True:
    print("You Win")
else:
    print("You Loose")
game(comp,player)