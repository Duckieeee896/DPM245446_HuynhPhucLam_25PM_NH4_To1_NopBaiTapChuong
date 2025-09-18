#Trả lời câu hỏi số 1 chương 2

import math

try:
    r=float(input("Nhap ban kinh hinh tron: "))
    cv=2*math.pi*r
    dt=r**2
    print("Chu vi:",round(cv))
    print("Dien tich:",round(dt))
except:
    print("Loi roi!")