x=int(input())
y=int(input())
z=int(input())
if(x>y) and (x>z):
  largest=x
elif(y>x) and (y>z):
  largest=y
else:
  largest=z
print(largest)
