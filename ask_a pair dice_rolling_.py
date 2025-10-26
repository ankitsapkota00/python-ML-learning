from random import randrange

check = "y"

while check =="y" or check != "n":

 check = input("Want to roll a dice? (y/n) ")
 
 if check == "y":
    print(randrange(1,7), randrange(1,7))

 elif check == "n":
    print("Thanks for playing") 

 else:
    print("Invalid choice")   
