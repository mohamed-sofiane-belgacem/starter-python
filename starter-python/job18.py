def myFunction( *paramètres ):
    myList = []

    for param in paramètres:
        if isinstance(param,(int)):
            myList.append(param)
            myList.sort()
    print(myList)

myFunction(1,25,48,56,11,42,87)
