
# (if)
age = int(input('อายุของคุณ : '))
if age >= 15:
    print('คำนำหน้าเป็น นาย / นางสาว')
print('จบโปรแกรม')

# (if..else)
age = int(input('อายุของคุณ : '))
if age >= 15:
    print('คำนำหน้าเป็น นาย / นางสาว')
else:
    print('คำนำหน้าเป็น เด็กชาย / เด็กหญิง')

print('จบโปรแกรม')

# (elif)
age = int(input('อายุของคุณ : '))
if age >= 15 and age < 20:
    print('วัยรุ่น')
elif age >= 20 and age < 40:
    print('วัยผู้ใหญ่')
elif age >= 40 and age < 60:
    print('วัยกลางคน')
elif age >= 60:
    print('วัยชรา')
else:
    print('วัยเด็ก')

# Ternary Operator
age = int(input('อายุของคุณ : '))
print('คำนำหน้าเป็น นาย / นางสาว') if age >= 15 else print('คำนำหน้าเป็น เด็กชาย / เด็กหญิง')

# if ซ้อน if
age = int(input('อายุของคุณ : '))
if age <= 0:
    if age == 0:
        print('เด็กน้อย')
    else:
        print('คุณป้อนอายุผิด')
else:
    print('เย้คุณโตแล้ว')

# pass
age = int(input('อายุของคุณ : '))
if age >= 15:
    pass
else:
    pass