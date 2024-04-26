# Assignment 10: หาผลรวมตัวเลข (ปรับเงื่อนไข)

sum = 0
while sum <= 100:
    number = int(input('ป้อนตัวเลข : '))
    sum += number
    print('ผลรวม : ', sum)

sum = 0
while True:
    if sum >= 100:
        break
    number = int(input('ป้อนตัวเลข : '))
    sum += number
    print('ผลรวม : ', sum)
