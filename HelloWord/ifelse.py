"""
age=int(input("enter your age"))
if age<=18:
    print("you are child")
elif 19<=age<40:
    print("you  are in middle age")
else:
    print('you are cinear citizen')
"""
# program for printing two digits , three digits , four digits numbers
digit=int(input("enter the number"))
if 9<digit<99:
    print("number two digit")
elif 99<digit<999:
    print("number is three digit")
elif 999<digit<9999:
    print("number is four digit")
else:
    print("number is <=9 and >=9999")
