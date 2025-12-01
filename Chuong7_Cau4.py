#Trả lời câu hỏi số 4 chương 7
import json 
jsonString =  '{ "ma":"nv1", "age":50, "ten":"Trần Duy Thanh"}'
dataObject=json.loads(jsonString) 
print(dataObject) 
print("Mã=",dataObject["ma"]) 
print("Tên=",dataObject["age"]) 
print("Tuổi=",dataObject["ten"])