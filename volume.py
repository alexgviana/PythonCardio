import math

def run():

    menu="""Welcome to the Volume calculator

        Select:
        1. Volume of cylinder
        2. Volume of sphere
        3. Volume of cube

    """

    sel=int(input(menu))

    if(sel==1):
        height=round(float(input("Enter the height of the cylinder: ")),2)
        rad=round(float(input("Enter the radius of the cylinder: ")),2)
        vol=round((math.pi*(rad**2)*height),2)
        print("The volume of cylinder is: " + str(vol))
    
    elif(sel==2):
        rad=round(float(input("Enter the radius of the sphera: ")),2)
        vol= round(((4/3*math.pi*(rad**3))),2)
        print("The volume of the sphere is: " + str(vol))
    
    elif(sel==3):
        edge=round(float(input("Enter the edge length of the cube: ")),2)
        vol=round((pow(edge,3)),2)
        print("The volume of the cube is: "+ str(vol))
    
    else:
        print("Wrong selection")


if __name__=="__main__":
    run()