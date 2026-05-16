def showbill():
    print("-------Yourmenu-------")
    for i in range(len(menulist)):
        print(menulist[i],(pricelist[i]))
    print("Total price is ",sum(pricelist))

menulist = []
pricelist = []
while True:
    menu =  input("Menu:")
    if menu.lower() == "exit":
        break
    else:
        price = int(input("Price:"))
        menulist.append(menu)
        pricelist.append(price)
showbill()