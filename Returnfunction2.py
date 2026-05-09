def Vatcalculate(price):
    result = price+(price*(7/100))
    return result
price = int(input("Enter your price: "))
print(Vatcalculate(price))