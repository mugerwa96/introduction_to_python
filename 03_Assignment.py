# check if the list is not empty

def checkLIst(list):
    if len(list) == 0:
        return 0
    elif len(list) == 4:
       return 4
# main code
list = []

if checkLIst(list)==0:
    i=0
    while(i<5):
        num=int(input("Enter number"))
        list.append(num)
        i+=1
        if(i==4):
            print("Maximum of elements reached")
            print("ELEMENTS IN AN ARRAY")
            for x in list:
                print(x)
elif checkLIst(list)==4:
    print("List is full")



