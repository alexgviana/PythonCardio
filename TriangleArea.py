def run():

    print("""Hi everyone, here you can calculate the area of a triangle and determinate if is equilateral, scalene or isosceles""")


    base=float(input("Type the base of the triangle: "))
    height=float(input("Type the height of the triangle: "))

    area =str(round(((base * height) / 2),2))

    print("The triangle area is: " + area)

    answ=int(input("If you know the others side of the triangle press 1, else press any other key: "))

    if(answ==1):
       
        side1=float(input("Type the side1: "))
        side2=float(input("Type the side2: "))
        
        if side1 == side2  and side1 == base:
            print("It is a equilateral triangle")
        
        elif side1 != side2 and side1 != base and side2!= base:
            print("It is a scalene triangle  ")

        else:
            print("It is a isosceles triangle ") 
    
    
    else:
        print("Goodbye!")        

    

if __name__ == "__main__":
    run()
