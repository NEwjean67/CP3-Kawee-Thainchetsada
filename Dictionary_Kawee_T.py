SystemMenu = {'nigger': 1 , 'siunaldo' : 100 , 'gyat':67}
menulist = []

def showbill():
    total = 0
    print("-------Yourmenu-------")
    for i in range(len(menulist)):
        print(menulist[i][0],menulist[i][1])
        total += menulist[i][1]

    print("Total price is ",total)

while True:
    menu =  input("Menu:")
    if menu.lower() == "exit":
        break
    else:
        if  menu.lower() in SystemMenu.keys():
            menulist.append((menu,SystemMenu[menu]))

showbill()