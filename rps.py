import  random

def run():


    menu= """
    You can play rocks, papers, scissors 
    
    Select
    1.Rocks
    2.Papers
    3.Scissors

    """

    usr= int(input(menu))

    user= {
        1:"Rocks",
        2:"Papers",
        3:"Scissors"
    }
    

    if(usr==1):
        print("Your choice is: " + (user[1]) )
    elif(usr==2):
       print("Your choice is: " + (user[2]) )
    elif(usr==3):
        print("Your choice is: " + (user[3]) )
    else:
        print("Wrong option selected")


    comp={
        1: "Rocks",
        2: "Papers",
        3: "Scissors"
    }

    ecomp=random.choice(list(comp.items()))
    
    print("The computer choice is: " + str(ecomp[1]))

    

    if (usr==1 and ecomp[0]==1):
        print("Is a draw")
    elif(usr==1 and ecomp[0]==2):
        print("The computer won")
    elif(usr==1 and ecomp[0]==3):
        print("You won")
    elif (usr==2 and ecomp[0]==1):
        print("You won")
    elif(usr==2 and ecomp[0]==2):
        print("Is a draw")
    elif(usr==2 and ecomp[0]==3):
        print("The computer won")
    elif(usr==3 and ecomp[0]==1):
        print("The computer won")
    elif(usr==3 and ecomp[0]==2):
        print("You won")
    else:
        print("Is a draw")




if __name__ == "__main__":
    run()
