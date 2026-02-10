# with open("My_image.png","rb")as file:
#     print(file.read())
#     data=file.read()
#     print(type(data))
#     print(len(data))
with open("students.csv","r")as file:
    rows = file.readline()
    print("total rows:", len(rows)-1)

with open("students.csv","r")as file:
    col = file.readline().strip().split(",")
    print("total numbers of column: ",len(col))

#display the first 5 records of file

with open("students.csv","r")as file:
    for i in range(6):
        print(file.readline().split())

with open("students.csv","r")as file:
    content = file.read()
print("tatal chars: ",len(content))

with open("students.csv","r")as file:
    content=file.read()

with  open("students.csv","w")as file:
    file.write(content)  