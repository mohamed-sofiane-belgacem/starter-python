
def myFunction( *params ):
    myList = []
    
    for parametre in params:
        if isinstance(parametre,(int)):
            myList.append(parametre)
    
        for element in myList:
            if element % 2 == 0:
                print (element)

myFunction(1,12,56,41,8,7,9,44,45,68)



