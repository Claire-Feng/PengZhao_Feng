'''
Name: PengZhao Feng
Student ID: 0891248
Due Date: 11/19/2019
Class: MSITM 6341
'''


def clamp(value, min, max):
    if value < min:
        return min
    elif max < value:
        return max
    else:
        return value
    
print(clamp(24, 35, 78))


