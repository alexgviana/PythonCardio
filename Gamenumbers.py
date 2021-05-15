def run():
    
    uppl=int(input("Enter the number of upper limit: "))
    lowl=int(input("Enter the number of lower limit: "))
    numb=int(input("Enter the number game: "))

    while numb >= uppl or numb <= lowl:
        print("Your number is: "+ str(numb))
        numb=int(input("Enter other number: "))
    
    print("The winner number is: " + str(numb))
    

if __name__=="__main__":
    run()