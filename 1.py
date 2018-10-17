#simple calculator


n=int(input("What is your choice ?? \n 1.Addition \n 2.Subtraction \n 3.Multiplication \n 4.Division \n"))
if(n==1):
	a=int(input("Enter A value :"))
	b=int(input("Enter B value :"))
	print(a+b)
elif(n==2):
	a=int(input("Enter A value :"))
	b=int(input("Enter B value :"))
	print(a-b)
elif(n==3):
	a=int(input("Enter A value :"))
	b=int(input("Enter B value :"))
	print(a*b)
if(n==4):
	a=int(input("Enter A value :"))
	b=int(input("Enter B value :"))
	print(a/b)

