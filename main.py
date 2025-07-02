import random 
computer = random.choice([-1,0,1])
youstr = input("ENTER THE CHOICE :")
youDict =  {"s":1,"w":-1,"g":0}
revdict = {1 : "SNAKE",-1: "WATER",0 :"GUN"}

you =youDict[youstr]

# by nkow we have two variables that was you and computer 

print(f"YOU CHOOSE {revdict[you]}\n COMPUTER CHOOSE {revdict[computer]}")

if (computer == you ):
    print("ITS A DRAW!")

else:
    
    if(computer == -1 and you == 1):
         print("YOU WON!")
         
    elif(computer == -1 and you == 0):
         print("YOU LOOSE!")

    elif(computer == 1 and you == 0):
         print("YOU WON!")

    elif(computer == 1 and you == -1):
         print("YOU LOOSE!")
         
    elif(computer == 0 and you == -1):
         print("YOU WIN!")

    elif(computer == 0 and you == 1):
         print("YOU LOOSE!")


    else:
         print("somegthing went wrong")
         
         
# ### short cut


# if(computer-you == -1 or 2):
    #  print("YOU LOSE")   

    # else:
    #  print("YOU WON")