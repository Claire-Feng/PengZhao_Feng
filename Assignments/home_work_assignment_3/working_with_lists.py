grocery_items = ['Grape', 'Strawberry', 'Cherry','Tomato', 'Avacado']
grocery_prices = [5.00,2.00,7.00,1.00,3.00]
#1.	Print the 3rd item followed by it’s price
print(grocery_items[2] + " " + str(grocery_prices[2]))
#2.	Print the last item followed by it’s price
print(grocery_items[len(grocery_items)-1] + " " + str(grocery_prices[len(grocery_prices)-1]))
#3.	Add a 6th item and it’s price
grocery_items.append("Icecream")
grocery_prices.append("4.00")
#4.	Print the list of items
print(grocery_items)
#5.	Print the list of prices
print(grocery_prices)
#6.	Remove the first item and it’s price
del grocery_items[0]
del grocery_prices[0]
#7.	Double the price of the 2nd item
grocery_prices[1] = grocery_prices[1] * 2
#8.	Print the list of items
print(grocery_items)
#9.	Print the list of prices
print(grocery_prices)
