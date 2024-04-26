# Assignment 13: สร้างภาพวาดสี่เหลี่ยมจตุรัส
'''
input = 5
xxxxx
xxxxx
xxxxx
xxxxx
xxxxx
'''

number = int(input('ป้อนตัวเลข : '))
for row in range(number):
    for column in range(number):
        print('x', end='') #คำสั่ง end='' ให้แสดงแนวนอน
    print(" ")