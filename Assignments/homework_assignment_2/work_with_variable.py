'''
Name: PengZhao Feng
Student ID: 0891248
Due Date: 09/08/2019
Class: MSITM 6341
'''

#Variable of Stock Sybol
stock_symbol = "appl"
#Variable of Price
price = 204.66
#Variable of Price
change = 4.08
#Dollar Amount Calculation formula
dollar_amount_changed = price - change

#Output_1
print("symbol:" + stock_symbol.upper() + ", " + "Price:" + str(price) + ", " + "Change:" + str(-change))
#Output_2
print("symbol:" + stock_symbol.lower() + ", " + "Price:" + str('${}'.format(price))+", "+"Change:"+ str(-change))
#Output_3
print("symbol:" + stock_symbol.upper() + " --- " + "Yesterday's price:" + str ("%.2f" % dollar_amount_changed))
