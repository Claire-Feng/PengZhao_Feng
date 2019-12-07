'''
Name: PengZhao Feng
Student ID: 0891248
Due Date: 12/7/2019
Class: MSITM 6341
'''

import re

fileName = 'test.txt'

# open a file with name 'test.txt'
with open(fileName, 'w+') as f:
    #  read()
    s = f.read()
    # equals s with None || "" ,this option
    if str(s) is "" or s is None:
        print('No store information found.')
        strInput = input('Enter the email address you would like to store?')
        # match()
        if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", strInput):
            print('Email address is Right!')
            with open(fileName, 'w') as fw:
                fw.write(strInput)
            print('Information saved.')
        else:
            print('Please reset your right Email address!')
            print('Information was not saved.')
    else:
        print("Email address loaded: " + s)
# close your file and end function
f.close()