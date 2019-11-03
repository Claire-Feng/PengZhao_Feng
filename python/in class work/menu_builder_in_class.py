menu_items = {}

should_ask_for_item = True

while should_ask_for_item:

    item = input("Item Name: ")
    cost = input("Item Cost: ")

    if item in menu_items:
        print("WARNING: Item exist")

    menu_items[item] = cost

    continue_or_not = input("Comtinue(Y/N)? ")

    if continue_or_not == "N":
        should_ask_for_item = False

print(menu_items)

def print_menu(menu_to_print):
   for item, cost in menu_items.items():
        print("Item Name: " + item + "Cost: " + str(cost))

