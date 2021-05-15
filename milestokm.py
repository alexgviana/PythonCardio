def run():
    
    menu="""Welcome to the convertion System
    
        Select:
        1. Convert miles to km
        2. Convert km to miles

    """

    sel=int(input(menu))

    if(sel==1):
        mil=round(float(input("Enter the miles: ")),3)
        km= round((mil*1.609344),3)
        print(str(mil) + " miles are " + str(km) + " kilometers")

    elif(sel==2):
        km=round(float(input("Enter the kilometers: ")),3)
        mil=round((km*0.6213710),3)
        print(str(km) + " kilometers are "+ str(mil)+ " miles")

    else:
        print("Wrong selection")
    
if __name__=="__main__":
    run()