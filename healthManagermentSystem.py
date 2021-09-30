import datetime
def gettime():
    return datetime.datetime.now()
def take(k):   
    if k==1:
        c=int(input("Enter 1 for Exercise and 2 for Food \n "))
        if c==1:
            value=input("Type here \n")
            with open("vishal-ex.txt","a") as op:
                op.write(str([str(gettime())]) + " : " + value + " \n ")
            print("Sucessfully written")

        elif c==2:
            value= input("Type here \n")
            with open("vishal-food.txt","a") as op:
                op.write(str([str(gettime)])+ " : " + value + " \n ")
            print("Sucessful written")
    elif k==2:
        c=int(input("Enter 1 for Exercise and 2 for Food \n "))
        if c==1:
            value=input("Type here \n")
            with open("prashant-ex.txt","a") as op:
                op.write(str([str(gettime())]) + " : " + value + " \n ")
            print("Sucessfully written")

        elif c==2:
            value= input("Type here \n")
            with open("prashant-food.txt","a") as op:
                op.write(str([str(gettime)])+ " : " + value + " \n ")
            print("Sucessful written")

    elif k==3:
        c=int(input("Enter 1 for Exercise and 2 for Food \n "))
        if c==1:
            value=input("Type here \n")
            with open("shivam-ex.txt","a") as op:
                op.write(str([str(gettime())]) + " : " + value + " \n ")
            print("Sucessfully written")

        elif c==2:
            value= input("Type here \n")
            with open("shivam-food.txt","a") as op:
                op.write(str([str(gettime)])+ " : " + value + " \n ")
            print("Sucessful written")

    else:
        print("Please enter valid input 1 (Vishal) , 2 (Prashant), 3 (Shivam)")

def retrieve(k):
    if k==1:
        c=int(input("Enter 1 for Exercise and 2 for Food \n"))
        if c==1:
            with open("vishal-ex.txt")as op:
                for i in op:
                    print(i, end=" ")
        elif c==2:
            with open("vishal-food.txt")as op:
                for i in op:
                    print(i, end=" ")

    elif k==2:
        c=int(input("Enter 1 for Exercise and 2 for Food \n"))
        if c==1:
            with open("prashant-ex.txt")as op:
                for i in op:
                    print(i, end=" ")
        elif c==2:
            with open("prashant-food.txt")as op:
                for i in op:
                    print(i, end=" ")
    
    elif k==3:
        c=int(input("Enter 1 for Exercise and 2 for Food \n"))
        if c==1:
            with open("shivam-ex.txt")as op:
                for i in op:
                    print(i, end=" ")
        elif c==2:
            with open("shivam-food.txt")as op:
                for i in op:
                    print(i, end=" ")

    else:
        print("Please enter valid input (Vishal ,Prashant ,Shivam)")

print("Health Managment System")
a= int(input("Press 1 for write the Value and 2 for retrive \n"))

if a==1:
    b= int(input("Press 1 for Vishal\n 2 for Prashant\n 3 for Shivam "))
    take(b)
else:
    b= int(input("Press 1 for Vishal\n 2 for Prashant\n 3 for Shivam "))
    retrieve(b)
