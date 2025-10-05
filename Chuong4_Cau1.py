#Trả lời câu hỏi số 1 chương 4
from math import sqrt
print("Chuong trinh tinh cong thuc tam giac")
a = float(input("Nhap canh a: "))
b = float(input("Nhap canh b: "))
c = float(input("Nhap canh c: "))
cv = a + b + c
p = cv / 2
dt = sqrt(p * (p - a) * (p - b) * (p - c))
print("Chu vi tam giac la: ", cv)
print("Dien tich tam giac la: ", dt)

