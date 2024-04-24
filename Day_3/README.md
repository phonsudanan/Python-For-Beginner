#### เจาะลึก String
String อยู่ในเครื่องหมาย double quote หรือ single quote
การเข้าถึงตัวอักษร Index เริ่มต้นที่ 0 เวลาเรียกใช้ name[] <-- เรียก Index 

ระบุตำแหน่งที่ต้องการเข้าถึง ดังนี้

```python
name = 'phonsuda'
print(name[3]) #ระบุตำแหน่งตัวเดียว
print(name[3:5]) #ระบุตำแหน่งเริ่มและก่อนจบ (ก่อนถึง 5 แสดงตำแหน่งที่ 3 และ 4)
print(name[-1]) #นับจากด้านหลัง -1 คือ a
print(name[-4:]) #แสดง suda นับจากด้านหลัง เริ่ม -1
```
len ใช้นับจำนวน String
```python
name = 'phonsuda'
print(len(name)) #8
```

strip ลบช่องว่าง หน้า-หลัง
```python
name = '  phonsuda  '
name = name.strip() #phonsuda
```
จัดการ แปลงข้อความ String
```python
name = 'PhOnSuDa NaLoEnG'
print(name.upper()) #พิมพ์ใหญ่ทั้งหมด
print(name.lower()) #พิมพ์เล็กทั้งหมด
print(name.capitalize()) #พิมพ์ใหญ่เฉพาะตัวแรก
```
แทนที่ข้อความ replace('ข้อความเดิม', 'ข้อความใหม่', จำนวนที่ต้องการเปลี่ยน ถ้าไม่ใส่จะเปลี่ยนทั้งหมด)
```python
name = 'phonsuda naloeng'
print(name.replace('a', 'nan', 1))
```

in เช็คว่ามีคำนี้อยู่ใน ข้อความหรือไม่ มีค่าเป็น True หรือ False สามารถนำไปใช้ต่อ ใน if ได้
```python
name = 'phonsuda naloeng'
x = "na" in name
if x:
    name = name.replace('na', 'nan')
```
การต่อ String ใช้เครื่องหมาย +
การจัดรูปแบบโดยใช้ เครื่องหมาย {}
```python
fname = 'nan'
lname = 'naloeng'
age = '20'
taxt = 'ชื่อจริง {} นามสกุล {} อายุ {} '
print(taxt.format(fname, lname, age))

taxt = 'ชื่อจริง {1} นามสกุล {1} อายุ {2} ' #ระบุตำแหน่ง
print(taxt.format(fname, lname, age))
```
การนับจำนวนคำในประโยค ใช้คำสั่ง count()
```python
fruit = 'ทุเรียน อะโวคาโด มังคุด แก้วมังกร สับปะรด มะพร้าว มะนาว ทุเรียน กล้วย อินทผลัม ทุเรียน'
print(fruit.count('ทุเรียน'))
```
startswith() เช็คคำขึ้นต้น  มีค่าเป็น True หรือ False

endswith() เช็คคำลงท้าย มีค่าเป็น True หรือ False