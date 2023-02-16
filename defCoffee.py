# 1 => Americano
# 2 => Espresso
# 3 => Cappuccino

#define the coffee() function
choice = int(input())
def coffee():
    if  choice == 1:
        print("Americano")
    elif choice == 2:
        print("Espresso")
    elif choice == 3:
        print("Cappuccino")
    else:
        print("Unknown")

coffee()