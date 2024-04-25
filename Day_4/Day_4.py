i = 1
while i <= 5:
    print('รอบที่ : ', i)
    i += 1

i = 1
sum = 0
while i <= 5:
    sum += i
    print ('รอบที่ : ', i ,'ผลรวม : ', sum)
    i += 1
print('ผลรวม : ', sum)

for i in range(10,1,-2):
    print('รอบที่ :', i)

i = 1
while i <= 3:
    print('รอบที่ i :', i)
    j = 1
    while j <= 5:
        print('รอบที่ j :', j)
        j += 1
    i += 1

for i in range(1,4):
    print('รอบที่ i :', i)
    for j in range(1,6):
        print('รอบที่ j :', j)

i = 1
while i <= 10:
    print('รอบที่ : ', i)
    if i == 5:
        break;
    i += 1

i = 0
while i <= 10:
    i += 1
    if i == 5:
        continue;
    print('รอบที่ : ', i)

for i in range(1,11):
    if i % 2 != 0:
        continue;
    print('รอบที่ : ', i)
