# # with open("My_image.png","rb")as file:
# #     print(file.read())
# #     data=file.read()
# #     print(type(data))
# #     print(len(data))
# with open("students.csv","r")as file:
#     rows = file.readline()
#     print("total rows:", len(rows)-1)

# with open("students.csv","r")as file:
#     col = file.readline().strip().split(",")
#     print("total numbers of column: ",len(col))

# #display the first 5 records of file

# with open("students.csv","r")as file:
#     for i in range(6):
#         print(file.readline().split())

# with open("students.csv","r")as file:
#     content = file.read()
# print("tatal chars: ",len(content))

# with open("students.csv","r")as file:
#     content=file.read()

# with  open("students.csv","w")as file:
#     file.write(content)  
def replace_good_boy_with_bad_boy():
    import pandas as pd
    df = pd.read_csv('students.csv')
    df['Name'] = df['Name'].replace('Anita', 'Mondeep')
    df.to_csv('students.csv', index=False)
    print(df)
# replace_good_boy_with_bad_boy()
# import pandas as pd

# def delete_bad_boy():
#     df = pd.read_csv('students.csv')
#     # Replace Mondeep with another name
#     df['Name'] = df['Name'].replace('Mondeep', 'New Name') 
#     df.to_csv('students.csv', index=False)

# delete_bad_boy()
# # how to delete a record row by only using name in python 
with open("students.csv",'a')as file:
    file.write("\n31,Ramesh,22,Male,Python,86")
# print('Record update sucessfully')
delete = "Ramesh"
with open("students.csv",'r')as file:
    lines = file.readlines()
with open("students.csv",'w')as file:
    for rec in lines:
        if delete not in rec:
            file.write(rec)
# print('Record Deleted')
with open('students.csv','r')as file:
    lines = file.readlines()
with open("name_score.csv","w")as new_file:
    new_file.write("Name,Score\n")
    for line in lines[1:]:
    
        data=line.strip().split(",")
        if len(data)>=2:
            new_file.write (f"{data[1]};{data[-1]}\n")
# print("Hoyegeche")