#print the average and tell the grade

print("\n Enter the three marks of the student : ")
a=int(input("\n Enter the mark 1:"))
b=int(input("\n Enter the mark 2:"))
c=int(input("\n Enter the mrk 3:"))
avg=(a+b+c)/3
print(avg)
if(avg>90):
	print("\n Your grade is O ")
elif(avg>80):
	print("\n Your grade is A ")
elif(avg>70):
	print("\n YOur grade is B ")
elif(avg>60):
	print("\n Your grade is C ")
elif(avg<60):
	print("\n Bettur luck next time ")
