# Shopping Cart - Ganesh Baral

# Clear console
import os
def clear(): os.system('cls')

# Import time 
import time

# Begin main()
def main():

    clear()
    # Main Menu Loop
    loop = True
    while loop:
        selection = displayMenu()

        # Output Based on Selection
        if selection == "1":
            addToCart()
        elif selection == "2":
            removeFromCart()
        elif selection == "3":
            displayCart()
        elif selection == "4":
            clearCart()
        elif selection == "5":
            checkOut()
        elif selection == "6":
            print("\nHave a great day!")
            loop = False
        else:
            print("\nInvalid menu selection")
# End main()
    
    
# Get Menu Selection
def displayMenu(): 
    print()
    print("Please make a selection.")
    print()
    print("1: Add an item to cart.")
    print("2: Remove an item from cart.")
    print("3: Display items in cart.")
    print("4: Clear your cart and start over.")
    print("5: Calculate total and checkout.")
    print("6: Exit")

    return input("What would you like to do?: ")
    
# End Get Menu Selection

# Create Shopping Cart List
shoppingCart = []
cartTotal = 0
    
def checkStock():
    clear()
    print()
    print("CURRENTLY IN STOCK: ")
    print("GTX 1050 TI")
    print("RTX 2060 SUPER")
    print("RTX 2080 TI")
    print("RTX 3070 TI")

def addToCart():
    checkStock()
    global cartTotal
    item = input("Enter name of your desired item: ")
    if item == "GTX 1050 TI":
        shoppingCart.append("GTX 1050 TI")
        cartTotal += 319.99
        print(item + " has been added to your cart!")
    elif item == "RTX 2060 SUPER":
        shoppingCart.append("RTX 2060 SUPER")
        cartTotal += 699.99
        print(item + " has been added to your cart!")
    elif item == "RTX 2080 TI":
        shoppingCart.append("RTX 2080 TI")
        cartTotal += 999.99
        print(item + " has been added to your cart!")
    elif item == "RTX 3070 TI":
        shoppingCart.append("RTX 3070 TI")
        cartTotal += 899.99
        print(item + " has been added to your cart!")
    else:
        print("Invalid Item. Please try again.")
    time.sleep(2.5)
    clear()
    
        
def removeFromCart():
    print("Your cart:")
    displayCart()
    global cartTotal
    item = input("Enter the name of the item you would like to take out: ")
    if item == "GTX 1050 TI":
        cartTotal -= 319.99
        shoppingCart.remove(item)
        print(item + " has been removed from cart.")
    elif item == "GTX 1050 TI":
        cartTotal -= 699.99
        shoppingCart.remove(item)
        print(item + " has been removed from cart.")
    elif item == "GTX 1050 TI":
        cartTotal -= 999.99
        shoppingCart.remove(item)
        print(item + " has been removed from cart.")
    elif item == "GTX 1050 TI":
        cartTotal -= 899.99
        shoppingCart.remove(item)
        print(item + " has been removed from cart.")
    else:
        print("Invalid item or there is nothing in the cart. Please try again.")
    time.sleep(2.5)
    clear()


def displayCart():
    clear()
    print("Current item(s) in cart:")
    print(shoppingCart)

def clearCart():
    global cartTotal
    clear()
    shoppingCart.clear()
    cartTotal = 0
    print("Your cart has been cleared.")

def checkOut():
    clear()
    print("Your total today is $", cartTotal)
    answer = input("Would you like to check out or continue shopping(y/n): ")
    if cartTotal == 0:
        print("You have nothing in cart. Bringing you back to the home page.")
        time.sleep(2.5)
        clear()
    else:
        if answer == "y":
            print("Thank you for shopping with us today!")
            time.sleep(2.5)
            clear()
        elif answer == 'n':
            print("Bringing you back to the home page!")
            time.sleep(2.5)
            clear()
    

main()