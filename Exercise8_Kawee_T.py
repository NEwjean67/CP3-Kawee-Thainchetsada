rus = "Hello World"
rps = "1234"
us = input("Enter your username: ")
ps = input("Enter your password: ")
if us == rus and ps == rps:
    print("correct")
    print("     * Fikau shop *   ")
    print("--------------------------")
    print("1. skibid toilet")
    print("2. ohio finalboss")
    eat = int(input("Your order:"))
    if eat == 1:
        num = int(input("How many do you want?"))
        print("calculate success")
        print(100*num,"bath")
    elif eat == 2:
        num2 = int(input("How many do you want"))
        print("calculate success")
        print(500*num2,"bath")
    else:
        print("we dont have that order!?")
print("thanks you")
