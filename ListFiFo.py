gwapo = []
cursor = 0
def outmeNot(lst):
    print("Mao ni ang listahan sa mga gwapo")
    for i in lst:
        print(i , end=", ")
    print("\n")

def inmeYes(x):
    newGwapo = []
    ask = 0
    while(not(ask >= 1 and ask <= 10)):
        ask = int(input("how many gwapo you would like to enter?>> "))
        if(not(ask >= 1 and ask <= 10)):
            print("##########  Ilogical number we only stores 1-10 gwapo a day")
    
    for i in range(ask):
        name = input("Enter the gwapo no."+str(i+1)+" name>> ")
        newGwapo.append(name)

    if((10-len(gwapo)) >= len(newGwapo)):
        gwapo.extend(newGwapo)
        x = len(gwapo)
    elif(len(gwapo) >= 10):
        for i in range(len(newGwapo)):
            if x > 9:
                x = 0
                gwapo[x] = newGwapo[i]
                x += 1
            else:
                gwapo[x] = newGwapo[i]
                x += 1
         
    return x ## magreturn x  ta para ang value sa atong cursor ma update.

def searchMebebe(lst, name):
    
    

    for i in range(len(lst)):
        if lst[i] == name:
            return True, name ## duha kabook atong return tan.awa pud digto sa atong code duha pud ang modawat
    return False, name
    
def updateMeOneMoreTime(lst):
    newName = "" # to avoid an error
    eupdate = input("Kinsa na gwapo emong e.update>>> ")

    naa, ngalan = searchMebebe(lst,eupdate)
    if naa:
        print(eupdate,"FOUND!")
        newName = input("Enter the new name of our new gwapo:")
        for i in range(len(lst)):
            if lst[i] == ngalan:
                return i, newName, naa
    else:
        return 0 , newName , naa
    
    
while(True):
    print("--- This is my listahan ng mga GWAPO ---")
    print("[1] - Insert Value")
    print("[2] - Search Value")
    print("[3] - Update Value")
    print("[4] - Traverse Value")
    print("[5] - Exit")
    menu = int(input("Enter choice >> "))
    if(menu == 5):
        print("Thank you---")
        break
    elif(menu == 1):
        cursor = inmeYes(cursor)
    elif(menu == 2):
        gepangita = input("Enter the name of gwapo you are looking>>> ")
        tinood, ngalan = searchMebebe(gwapo,gepangita)
        if tinood:
            print(ngalan ,"is a CERTIFIED GWAPO")
        else:
            print(ngalan, "---- Dili na siya gwapo")
    elif(menu == 3):
        aha , name, up = updateMeOneMoreTime(gwapo)
        if up:
            gwapo[aha] = name
            print("index",aha,"Successfully updated to",name)
        else:
            print("cannot update because not a certified gwapo")
    elif(menu == 4):
        outmeNot(gwapo)
    else:
        print("Invalid input .... \n Please try again")
