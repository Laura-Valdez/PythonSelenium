a=40
b=10.5
c=20

### condition
if(a<b):
    print("the oldest is " +str(a))
else:
    print("the minor is " + str(b))

name ="Jun"
if(name=="Juan"):
        print("your name is "+name)


if(a>b and a>c):
    print(" the older one is : "+ str(a))
elif(b>a and b>c):
    print(" the older one is : " + str(b))
elif(c>a and c>b):
    print(" the older one is "+ str(c))
else:
    print("it's same ")

if(a>b or a>c):
    print(" {} <{} o {} >{} : ".format(a,b,a,c))
