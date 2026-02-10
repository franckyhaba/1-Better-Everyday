def getFullName(fName,sName, mName =''):
    if mName:
        fullName = f"\n {fName} {mName}{sName}"
    else:
        fullName = f"\n {fName} {sName}"
    return fullName.title()

footy = getFullName('jimi','jon','Mac')
print(footy)
footy = getFullName('jimi','Mac')
print(footy)