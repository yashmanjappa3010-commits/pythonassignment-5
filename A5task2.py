lists1=[1,2,3,4,5,6,7,8,9,10]
lists2=[]
lists3=[]
print(f"original list= {lists1}")

for i in lists1[0:5]:
    lists2.append(i)
print(f"Extracted first five elements from the list:{lists2}")
for i in lists2[5: :-1]:
    lists3.append(i)

print(f"reversed list:{lists3}")


