a=["apple","banana","orange"]
b=["cabbage","papaya","pineapple"]
c=[a,b]
for x in c:
 if isinstance(x,list) == True:
  for y in x:
   print(y)
 else :
   print(x) 
