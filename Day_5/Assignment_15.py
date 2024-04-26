# Assignment 15: สร้างขอบตาราง
'''
input = 5
xxxxx
x   x
x   x
x   x
xxxxx
'''

number = int(input('ป้อนตัวเลข : '))
for row in range(1,number+1):
    for column in range(1,number+1):
        if row == 1 or row == number or column == 1 or column == number:
            print('x', end='')
        else:
            print(' ', end='')
    print(" ")