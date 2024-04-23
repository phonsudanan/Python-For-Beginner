# โปรแกรมคำนวณค่า BMI

weight = int(input('ป้อนน้ำหนักของคุณ (kg) : '))
high = int(input('ป้อนส่วนสูงของคุณ (cm) : ')) / 100 # แปลงส่วนสูงจาก เซนติเมตร เป็น เมตร

bmi = weight / (high**2) #(high*high)
print('ค่าที่ได้ : ', bmi)