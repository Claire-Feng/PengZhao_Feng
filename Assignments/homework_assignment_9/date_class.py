'''
Name: PengZhao Feng
Student ID: 0891248
Due Date: 11/24/2019
Class: MSITM 6341
'''

class Date():
    def _init_ (self):
        self.day = ""
        self.month = ""
        self.year = ""
    
    def print_date(self):
        print(self.month + "" + str(self.day) + "," + " " + str(self.year))

    def change_date(self,day,month,year):
        self.day = day
        self.month = month
        self.year = year

my_date = Date()
my_date.day = 19
my_date.month = "June"
my_date.year = 2019

my_date.print_date()

my_date.change_date(3,"Augest",2019)
my_date.print_date()
