# check if the list is not empty

def checkLIst(list):
    if len(list) == 0:
        return 0
    else:
        return 1


# main code
number = []
if checkLIst(number):
    print("List i empty")
else:
    print("ITs ok")
