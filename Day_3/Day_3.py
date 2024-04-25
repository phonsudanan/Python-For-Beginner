name = '  phonsuda  '
print(name[3]) #ระบุตำแหน่งตัวเดียว
print(name[3:5]) #ระบุตำแหน่งเริ่มและก่อนจบ (ก่อนถึง 5 แสดงตำแหน่งที่ 3 และ 4)
print(name[-1]) #นับจากด้านหลัง -1 คือ a
print(name[-4:]) #แสดง suda นับจากด้านหลัง เริ่ม -1

print(len(name))

name = name.strip()
print(len(name))


name = 'PhOnSuDa NaLoEnG'
print(name.upper()) #พิมพ์ใหญ่ทั้งหมด
print(name.lower()) #พิมพ์เล็กทั้งหมด
print(name.capitalize()) #พิมพ์ใหญ่เฉพาะตัวแรก

name = 'Phonsuda naloeng'

x = "na" in name
print(x)
if x:
    name = name.replace('na', 'nan')
    print(name)

fname = 'nan'
lname = 'naloeng'
age = '20'

taxt = ' ชื่อจริง ' + fname + ' นามสกุล ' + lname + ' อายุ ' + age
print(taxt)

taxt = 'ชื่อจริง {} นามสกุล {} อายุ {} '
print(taxt.format(fname, lname, age))

fruit = 'ทุเรียน อะโวคาโด มังคุด แก้วมังกร สับปะรด มะพร้าว มะนาว ทุเรียน กล้วย อินทผลัม ทุเรียน'
print(fruit.count('ทุเรียน'))
print(fruit.startswith('ทุเรียน'))
print(fruit.endswith('เรียน'))