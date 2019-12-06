'''
Name: PengZhao Feng
Student ID: 0891248
Due Date: 12/1/2019
Class: MSITM 6341
'''

def maximum_difference():
    lst = []
    num = int(input("How many numbers?"))
    for lst in range(0, num):
        ele = int(input())
        lst.append(ele)

    abstract = max(lst) - min(lst)
    print("Maximum difference is: " + str(abstract))


maximum_difference()