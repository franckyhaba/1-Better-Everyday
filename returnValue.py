def getFullName(fName,mName ,sName):
    
    fullName = f"\n {fName} {mName}{sName}"
    return fullName.title()

footy = getFullName('jimi','jon','Mac')
print(footy)