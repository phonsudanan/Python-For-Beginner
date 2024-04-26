# Assignment 12: ตัวเลขขั้นบันได
'''
input = 5
1
12
123
1234
12345
'''

number = int(input('ป้อนตัวเลข : '))
for row in range(1,number+1):
    for column in range(1,row+1):
        print(column, end='') #คำสั่ง end='' ให้แสดงแนวนอน
    print(" ")