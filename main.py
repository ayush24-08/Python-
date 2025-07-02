import random
n = random.randint(1,100)
a= -1
guess = 1

while(a!= n):

    a = int(input("ENTER THE NUMBER :"))

    if(a>n):
        print("ENTER THE LOWER NUMBER :")
        guess += 1 

    elif(a<n):
        print("ENTER THE HIGHER NUMBER :")
        guess += 1 

print(f" THE NUMBER IS {n} AND THE NUMBER OF YOUR ATTEMPS IS {guess}")