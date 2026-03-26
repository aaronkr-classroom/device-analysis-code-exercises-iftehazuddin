#data_types.py
a=10
b=3.14
c="Hello"
d=True

print(f"{a} is a {type(a)}")
print(f"{b} is a {type(b)}")
print(f"{c} is a {type(c)}")
print(f"{d} is a {type(d)}")

#str
e='Odin'
f="Jotenheimn"
name=e+" "+f

g=name+" said, \"it's a beautiful day!!!!"
h='"how \'ya doin\' this yonder?"\n\t"Gnarly!"'
print(g, "\n",h)

#bool - only 0 or "" is FAlse
i=True
j=False
k=bool(-1)
l=bool(a)
m=bool("")
n=bool(0)
o=bool(g)

print(i,j,k,l,m,n,o)