def commaCode(myList):
    newString = ''       
    for x in myList:
        if x == myList[-1]:
            newString = newString + "and " + str(x)
        else:
            newString = newString + str(x) + ", "
    
    print(newString)
        


commaCode(['cats', 'dogs', 'tofu', 'god'])

            
