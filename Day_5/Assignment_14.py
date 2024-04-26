# Assignment 14: สร้างตารางหมากฮอต
'''
input = 5
xoxoxoxo
oxoxoxox
xoxoxoxo
oxoxoxox
xoxoxoxo
'''

number = int(input('ป้อนตัวเลข : '))
for row in range(number):
    for column in range(number):
        if (row+column) % 2 == 0:
            print('x', end='')
        else:
            print('o', end='')
    print(" ")

'''
เริ่มต้น row column = 0
รอบที่ 1 row = 0 column = 0  === x
รอบที่ 2 row = 0 column = 1  === o
รอบที่ 3 row = 0 column = 2  === x
รอบที่ 4 row = 0 column = 3  === 0
'''