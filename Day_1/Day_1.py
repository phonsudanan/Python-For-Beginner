#Comment บรรทัดเดียว

'''
Comment หลายบรรทัด
พิมพ์ข้อความด้านใน
'''

print('Hello World!')

print(-1)
print(0)
print(50.98)

print(True)
print(False)

x = 10
y = 20.789
z = x + y

print('ผลลัพธ์ \t', z)

x = 10
print(type(x))

x = 10
y = "20"
result_1 = x + int(y)
result_2 = str(x) + (y)

print('ผลลัพธ์ \t', result_1) #ผลลัพธ์ 	 30
print('ผลลัพธ์ \t', result_2) #ผลลัพธ์ 	 1020

fullName = input('กรุณาใส่ชื่อของคุณ : ')
print(fullName)

a = int(input("Number 1 : "))
b = int(input("Number 2 : "))
print('Number 1 + Number 2 : ', a+b) #Number 1 + Number 2 :  30

x = 25
y = 4

print('ผลบวก', x+y) #ผลบวก 29
print('ผลลบ', x-y) #ผลลบ 21
print('ผลคูณ', x*y) #ผลคูณ 100
print('ผลหาร', x/y) #ผลหาร 6.25
print('ผลหารปัดเศษ', x//y) #ผลหารปัดเศษ 6
print('ผลยกกำลัง', x**y) #ผลยกกำลัง 390625
print('ผลหารเอาเศษ', x%y) #ผลหารเอาเศษ 1

x, y = 25, 20

print(' ค่า X มากกว่า ค่า Y หรือไม่ : ', x>y) #True
print(' ค่า X น้อยกว่า ค่า Y หรือไม่ : ', x<y) #False
print(' ค่า X เท่ากับ ค่า Y หรือไม่ : ', x==y) #False
print(' ค่า X ไม่เท่ากับ ค่า Y หรือไม่ : ', x!=y) #True

print(' ค่า X มากกว่า หรือ เท่ากับ ค่า Y หรือไม่ : ', x>=y) #True
print(' ค่า X น้อยกว่า หรือ เท่ากับ ค่า Y หรือไม่ : ', x<=y) #False

x, y, z = 25, 20, 20

print(' ค่า X มากกว่า ค่า Y และ ค่า Y มากกว่า Z หรือไม่ : ', x>y>z) #False
print(' ค่า X มากกว่า ค่า Y และ ค่า Y มากกว่า หรือ เท่ากับ Z หรือไม่ : ', x>y>=z) #True

x = 5>2 
y = 2!=2

print(x and y) #หรือ print(x & y) False
print(x or y) #print(x | y) #True
print(not x or y) #False


x = 5 
print('ก่อนเพิ่มค่า : ', x) #ก่อนเพิ่มค่า :  5

x += 2 #เขียนค่าปกติ คือ x = x + 2
print('หลังเพิ่มค่า : ', x) #หลังเพิ่มค่า :  7

a = 5+3-2*4/2
print(a) #4.0

b = 5+(3-2)*4/2
print(b) #7.0



