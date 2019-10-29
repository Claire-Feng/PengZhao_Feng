'''
Name: PengZhao Feng
Student ID: 0891248
Due Date: 10/29/2019
Class: MSITM 6341
'''


menu = {
    "Chesse Burger": 8,
    "Potato Fried": 5,
    "Salad": 6,
    "Fried Chicken": 10,
    "Chiken Nuggets": 4
}

user_order = []
item_name = ''
total = 0

while item_name != 'N':
    item_name = input('Enter an item ')
    if item_name != 'N':
        user_order.append(item_name)
print('')
for item in user_order:
    if item in menu:
        itemPrice = menu.get(item)
        print("{}: ${:.1f}".format(item,itemPrice))
        total += itemPrice
    else:
        print('We do not have ' + item)

print("---------------------")
print("Order Total: ${:.1f}".format(total))