# check if the list is not empty

def checkLIst(list):
    if len(list) == 0:
        return "List empty"
    elif len(list) == 4:
        return "List Full"
    else:
        return 1


# main code
list = [2, 4, 5,4]
if checkLIst(list):
    print(checkLIst(list))
    if(checkLIst(list)==1):
        print("You can append")
    else:
        print("You cant append")
else:
    print("ok")
