a=["cherry","apple","banana","banana"]
a.sort()
print(len(a))
print(a)
b=[]
for x in a:
 if x not in b:
  b.append(x)
print(b)