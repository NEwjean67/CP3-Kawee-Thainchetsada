def showbill():
    total = 0
    print("-------Yourmenu-------")
    for i in range(len(menulist)):
        print(menulist[i][0],menulist[i][1])
        total += menulist[i][1]

    print("Total price is ",total)

menulist = []
while True:
    menu =  input("Menu:")
    if menu.lower() == "exit":
        break
    else:
        price = int(input("Price:"))
        menulist.append((menu,price))
showbill()