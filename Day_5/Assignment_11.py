# Assignment 11: ค้นหาตัวเลขมากสุด / น้อยสุด

number = int(input('ป้อนตัวเลข : '))
max = number
min = number
while True:
    number = int(input('ป้อนตัวเลข : '))
    if number < 0:
        break
    if number > max:
        max = number
    if number < min:
        min = number
print('ค่าสูงสุดคือ', max)
print('ค่าต่ำสุดคือ', min)