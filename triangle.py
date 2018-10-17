#type of triangle
print("\n Enter the three sides of the triangle :")
a=int(input())
b=int(input())
c=int(input())
if(a==b)and(b==c)and(c==a):
		print("\n It is equilateral triangle ")
elif(a==b)or(b==c)or(c==a):
	if(b!=c)or(a!=c)or(a!=b):
		print("\n It is isocleses triangle ")
else:
	print("\n It is a scalant triangle ")
