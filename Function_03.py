def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "admin" and passwordInput == "1234":
        return True
    else:
        return False

def main():
    print("----- iShop -----")
    print("1. Vat Calculator")
    print("2. Price Calculator")
    print("select and enter price")
def vatcalculate(totalprice):
    vat = 7
    result = totalprice + (totalprice * vat / 100)
    print(result)
def pricecalculate():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    return vatcalculate(price1 + price2)

if login():
    main()
    pricecalculate()
else:
    print("Login Failed")
