# Shopping Cart - Ganesh Baral

# Imports
import os
def clear(): os.system('cls') 
import time
import json

# lead previous saved file
try:
    with open("shopping_cart.txt") as save_file:
        shoppingCart = json.load(save_file)
except:
    shoppingCart ={
        "item": [],
        "cost": 0
    }
    print("No save files.")

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
            loop = False
            with open("shopping_cart.txt", "w") as save_file:
                json.dump(shoppingCart, save_file)
                print("\nHave a great day!")
        else:
            print("\nInvalid menu selection")
    
    
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
    print("6: Save your current cart and exit")

    return input("What would you like to do?: ")
    
# End Get Menu Selection

# Function that shows stock

def checkStock():
    clear()
    print()
    print("CURRENTLY IN STOCK: ")
    print("GTX 1050 TI, $319.99")
    print("RTX 2060 SUPER, $699.99")
    print("RTX 2080 TI, $999.99")
    print("RTX 3070 TI, $899.99")

# Add to cart function

def addToCart():
    checkStock()
    item = input("Enter name of your desired item: ")
    if item == "GTX 1050 TI":
        shoppingCart["item"].append("GTX 1050 TI")
        shoppingCart["cost"] += 319.99
        print(item + " has been added to your cart!")
    elif item == "RTX 2060 SUPER":
        shoppingCart["item"].append("RTX 2060 SUPER")
        shoppingCart["cost"] += 699.99
        print(item + " has been added to your cart!")
    elif item == "RTX 2080 TI":
        shoppingCart["item"].append("RTX 2080 TI")
        shoppingCart["cost"] += 999.99
        print(item + " has been added to your cart!")
    elif item == "RTX 3070 TI":
        shoppingCart["item"].append("RTX 3070 TI")
        shoppingCart["cost"] += 899.99
        print(item + " has been added to your cart!")
    else:
        print("Invalid Item. Please try again.")
    time.sleep(1)
    clear()

    

# remove from cart funciton

def removeFromCart():
    print("Your cart:")
    displayCart()
    item = input("Enter the name of the item you would like to take out: ")
    if item == "GTX 1050 TI":
        shoppingCart["cost"] -= 319.99
        shoppingCart["item"].remove("GTX 1050 TI")
        print(item + " has been removed from cart.")
    elif item == "RTX 2060 SUPER":
        shoppingCart["cost"] -= 699.99
        shoppingCart["item"].remove("RTX 2060 SUPER")
        print(item + " has been removed from cart.")
    elif item == "RTX 2080 TI":
        shoppingCart["cost"] -= 999.99
        shoppingCart["item"].remove("RTX 2080 TI")
        print(item + " has been removed from cart.")
    elif item == "RTX 3070 TI":
        shoppingCart["cost"] -= 899.99
        shoppingCart["item"].remove("RTX 3070 TI")
        print(item + " has been removed from cart.")
    else:
        print("Invalid item or there is nothing in the cart. Please try again.")
    time.sleep(1)
    clear()

# displays whats currently in cart

def displayCart():
    clear()
    
    print("Current item(s) in cart:")
    print(shoppingCart)

# clears current cart

def clearCart():
    clear()
    shoppingCart["item"].clear()
    shoppingCart["cost"] = 0
    print("Your cart has been cleared.")

# check out function

def checkOut():
    clear()
    print("Your item(s) and total cost today", shoppingCart)
    answer = input("Would you like to check out or exit(y/n): ")
    if answer == "y":
        print("Thank you for shopping with us today! Your order is estimated \n to arrive in 3-7 buisness days.")
        time.sleep(3)
        clear()
    elif answer == 'n':
        print("Exiting . . .")
        time.sleep(1)
        clear()
        exit()
        
        
# end main
main()
