#Trả lời câu hỏi số 1 chương 3
print("Chuong trinh kiem tra nam nhuan")
year = int(input("Nhap nam can kiem tra: "))
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("Nam" ,year, "La nam nhuan")
else:
    print("Nam" ,year, "Khong phai la nam nhuan")