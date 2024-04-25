# Assignment 8: แม่สูตรคูณ

for x in range(2,13):
    print('\nสูตรคูณ แม่ ', x)
    for y in range(1,13):
        print(x, 'x', y , '=', x*y)


start = int(input('ระบุแม่สูตรคูณที่ต้องการแสดง : '))
for x in range(start, start+1):
    print('\nสูตรคูณ แม่ ', start)
    for y in range(1,13):
        print(x, 'x', y , '=', x*y)
