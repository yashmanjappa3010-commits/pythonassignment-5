student={"nico":90 ,"alice":85 ,"wonderboy":96 ,"luffy":97 ,"zoro":74 ,"alex":65}
name=input("Enter the student's name:")
for i in student:
    if i==name:
         print(f" {i} marks is: {student[i]}")
else:
    print("student not found!!")