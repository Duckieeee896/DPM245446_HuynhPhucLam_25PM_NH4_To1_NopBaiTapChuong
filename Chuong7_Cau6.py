#Trả lời câu hỏi số 6 chương 7
import csv 
with open('datacsv.csv', newline='') as f: 
    reader = csv.reader(f, delimiter=';', quoting=csv.QUOTE_NONE) 
    for row in reader: 
        print(row[0],"\t",row[1]) 