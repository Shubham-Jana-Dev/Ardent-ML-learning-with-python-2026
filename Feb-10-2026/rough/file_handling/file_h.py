import os
with open ("sukalpa.txt","x")as file:
    print("File Created.")

vowels="aeiouAEIOU"
newch="b"
count = 0
with open ("sukalpa.txt","w")as file:
    file.write("Sukalpa Manna")
with open("sukalpa.txt","r")as file:
    print(file.read())
with open("sukalpa.txt","a")as file:
    file.write("\nI am a student")
with open("sukalpa.txt","r")as file:
    content = file.read()
    for char in content:
        if char in vowels:
            count += 1
print("Number of vowels:", count)
with open("sukalpa.txt","r")as file:
    content = file.read()
    new_content=content.replace("I am a student","I am an Engineer")
with open("sukalpa.txt","w")as file:
    file.write(new_content)
with open("sukalpa.txt","r")as file:
    new_content = file.read()
    for char in vowels:
        updated_content=new_content.replace(char,newch)
print(new_content)