# Assignment 4: โปรแกรมแยกธนบัตร

cash = int(input('ใส่จำนวนเงินที่ต้องการตรวจสอบ : '))

if cash >= 1000:
    one_thousand = cash // 1000
    print('จำนวนธนบัตร 1,000.00 บาท จำนวน : ', one_thousand, ' ใบ ')
    cash = cash % 1000

if cash >= 500:
    five_hundred = cash // 500
    print('จำนวนธนบัตร 500.00 บาท จำนวน : ', five_hundred, ' ใบ ')
    cash = cash % 500

if cash >= 100:
    one_hundred = cash // 100
    print('จำนวนธนบัตร 100.00 บาท จำนวน : ', one_hundred, ' ใบ ')
    cash = cash % 100

if cash >= 20:
    twenty = cash // 20
    print('จำนวนธนบัตร 20.00 บาท จำนวน : ', twenty, ' ใบ ')
    cash = cash % 20

print('เหรียญบาท จำนวน : ', cash, ' เหรียญ ')

