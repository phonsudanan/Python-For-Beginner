'''
Assignment 7: โปรแกรมแปลงอุณหภูมิ 
C = (F-32) * 5 / 9
F = (C*9/5) + 32
'''

temp = input('ระบุตัวเลขที่ต้องการแปลง (C/F) : ')
degree = int(temp[:-1])
unit = temp[-1].upper()

if unit == 'C':
    result = (degree*9/5) + 32
    unit_rusult = 'องศาฟาเรนไฮต์'

if unit == 'F':
    result = (degree-32) * 5 / 9
    unit_rusult = 'องศาเซลเซียส'

print('เลขที่ต้องการแปลงคือ : ', temp,  '\nแปลงได้เป็น : ', result, unit_rusult)