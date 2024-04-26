# Assignment 9: ป้อนตัวเลขหาผลรวมตัวเลข

start , stop = 1,5
sum = 0
while (start <= stop):
    number = int(input('ป้อนตัวเลขของคุณ : '))
    sum += number
    start += 1

avg = sum / stop
print('ผลรวม : ', sum)
print('ค่าเฉลี่ย : ', avg)