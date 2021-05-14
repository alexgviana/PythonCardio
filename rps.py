import  random

def run():

    countu=0
    countc=0

    while countu <=2 and countc <=2:

        menu= """
        Rocks, Papers or Scissor Game
    
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

        def resultado():
            print("You win " + str(countu) + " times")
            print("The computer win " + str(countc) + " times" )

        def cwin():
            print("The computer win")

        def uwin():
            print("You win")
            
        def draw():
            print("Is a draw")

        if (usr==1 and ecomp[0]==1):
            draw()
            resultado()

        elif(usr==1 and ecomp[0]==2):
            cwin()
            countc+=1
            resultado()       

        elif(usr==1 and ecomp[0]==3):
            uwin()
            countu+=1
            resultado()
            
        elif (usr==2 and ecomp[0]==1):
            uwin()
            countu+=1
            resultado()

        elif(usr==2 and ecomp[0]==2):
            draw()
            resultado()

        elif(usr==2 and ecomp[0]==3):
            cwin()
            countc+=1
            resultado()

        elif(usr==3 and ecomp[0]==1):
            cwin()
            countc+=1
            resultado()

        elif(usr==3 and ecomp[0]==2):
            uwin()
            countu+=1
            resultado()
        else:
            draw()
            resultado()
    
    

if __name__ == "__main__":
    run()
