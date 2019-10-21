'''
Name: PengZhao Feng
Student ID: 0891248
Due Date: 09/26/2019
Class: MSITM 6341
'''

#dictionary
menu = {
    "Chesse Burger": 8,
    "Potato Fried": 5,
    "Salad": 6,
    "Fried Chicken": 10,
    "Chiken Nuggets": 4
}

total = 0
cart = ['Salad', 'Potato Fried', 'Hot Pot', 'Chesse Burger']

for item in cart:    
    if item in menu:
        itemPrice = menu.get(item)
        print ("{} : ${:.1f}".format(item,itemPrice))
        total += itemPrice
    else:
        print ("We do not have {}".format(item))

print("---------------------")
print("Order Total: ${:.1f}".format(total))
