n= input()
l=list(n)
s=set(l)
if len(s)==len(l):
    print("Unique Number")
else:
    print("Not Unique Number")