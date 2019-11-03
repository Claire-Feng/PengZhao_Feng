'''
Name: PengZhao Feng
Student ID: 0891248
Due Date: 11/2/2019
Class: MSITM 6341
'''
menu_items = {}
should_ask_for_item = True
print("-----------------------------------------")
print("Please enter the menu items for the Restaurant")
print ("-----------------------------------------")

def print_menu():
    print("-----------------------------------------")
    print("Restaurant Menu")
    print("-----------------------------------------")
    for item, cost in menu_items.items():
       print("Item Name: {} Cost: ${:.1f}".format(item,cost))
def ask_user_for_menu_item_name():
    item = input("Item Name: ")
    return item
    #This function should prompt the user for "Item Name" and return the result.
def ask_user_for_menu_item_cost():
    cost = input("Item Cost: ")
    return cost
    #This function should prompt the user for "Item Cost" and return the result.
def add_menu_item(menu, item_name, cost) :
    if item_name in menu:
        print("WARNING: Item exists")
    else:
        menu[item_name] = cost
    #-This function should take as arguments the menu(dictionary), name of the item, and cost of the item
    #-It should then add the item to the menu, displaying a WARNING message if the item already exists

while should_ask_for_item:
    item_name = ask_user_for_menu_item_name()
    item_cost = ask_user_for_menu_item_cost()
    add_menu_item(menu_items,item_name,item_cost)
    continue_or_not = ""
    while continue_or_not != "Y" and continue_or_not != "N" :
        continue_or_not = input("Continue(Y/N)? ")
    if continue_or_not == "N":
        should_ask_for_item = False

print_menu()