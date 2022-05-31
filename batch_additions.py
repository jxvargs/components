#!usr/bin/env python3

# Jose V
# May 14th 2022.
# The following program, it is a tool to help
# adding batches and discarded componenets quantities.

#print("hello Mundo...!")
import os

def main():
    clear_screen()
    print(" Greetings, Dream Boat... ".center(35,'-'))
    ans = menu()
    menu_selection(ans)

# Menu display 
def menu() -> str: 
    answers = ['1','2','B','C']
    print('''
    1]- (B)lends.
    2]- (C)omponents.
    3]- E(x)it.
    ''')
    ans = input("Select option (1 - 3), (B, C, x): ")
    if ans in  answers:
        return ans
    elif ans == '3' or ans == 'x':
        os._exit(0) #it exits with status code 0, indicating success:
    else:
        input("Do you want to Exit? Press any key to continue...")
        clear_screen()
        main()

# Submenu selection 
def menu_selection(ans) -> None:
    if ans == '1' or ans == 'B':
        blends()
    elif ans == '2' or ans == 'C':
        components_entry()
    else:
        input("Do you want to Exit? Press any key to continue...")
        clear_screen()
        menu() 

# Displaying items to be entered
def components_banner() -> None:
    print('''
    1)- B(u)lk.
    2)- B(o)tellas.
    3)- D(i)secante.
    4)- N(e)ckBand.
    5)- E(x)it
    ''')
# This method will append items into the list and 
# it will display the grand total on screen.
def blends() -> None:
    clear_screen()
    flag = -1
    quantities = []
    print("Enter the amout of Tablest or Capsule per blend.")
    print(" or enter (-1) to exit.".center(50, '*'))
    quantity = int(input("-> "))

    # Appending quantities to the list while not equal to -1.
    while quantity != flag:
        quantities.append(quantity)
        quantity = float(input("-> "))
    print("\nDone\n")
    
    # Adding quantities of blends - grand total.
    total = total_qty_of_blend(quantities)
    # f-string formatting output , and .2 decimals
    print(f"\tTotal of Capusles/Tablets: {total:,.2f}")
    input("\nPress any key to continue...")
    clear_screen()
    main()

# Adding quantities elements in quantities list.
def total_qty_of_blend(quantities) -> int:
    total = 0
    for quantity in quantities:
        total += quantity
    
    return total
    
# Enter item name and append quantities to components list
def components_entry():
    components_banner()
    components = {
        'Bulk': [], 
        'Bottles': [], 
        'desiccant': [], 
        'neckband': []
        }
# Iterating the dict {} and updating each key - value. 
    for key in components.keys():
        print(f"{key}:")
        quantities = fill_quantities()
        components.update({key:quantities})
        print(f"\tTotal of {key}: {sum(quantities):,.2f}")
        print("-".center(25,'-'))

    input("\nPress any key to continue...") 
    clear_screen()
    main()
    
# Filling a list with quantities to be added.
def fill_quantities() -> int:
    flag = -1
    quantities = []
    quantity = int(input("-> "))
    
    while quantity != flag:
        quantities.append(quantity)
        quantity = int(input("-> "))
    
    return quantities

# Clearing screen as itself
# Note: Depending on your operating system
#    os.system("clear") unix like OS e.g Gnu/linux, macOS
#    os.system("cls") windows OS
def clear_screen():
    os.system("clear")

# Initialize program.
if __name__ == "__main__":
    main()
