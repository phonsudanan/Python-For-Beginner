# Assignment 16: เกมทายเลขลูกเต๋า

import random
myRandom = random.randrange(1,5)
print(myRandom)
myRound = 1
while True:
    if myRound > 3:
        print('คุณสุ่มได้แค่ 3 ครั้ง')
        break
    number = int(input('ป้อนตัวเลข : '))
    if number == myRandom:
        print('รับเงินรางวัล')
        break
    else:
        print('ยังไม่ถูก ลองใหม่อีกครั้งนะ')
        print('คำใบ้ :', number, 'น้อยกว่า') if number < myRandom else print('คำใบ้ :', number, 'มากกว่า') 
    myRound += 1