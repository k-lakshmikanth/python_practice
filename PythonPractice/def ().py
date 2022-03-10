fruits=["apple","banana","orange","cherry"]
roots=["carrots","beetroot","potato"]
vegetables=["cabbage","bottlegourd","tomato","onions",roots]
vegans=["eggs","mushrooms"]
nonvegetables=["chicken","mutton","fish"]
eatables=[fruits,vegetables,vegans,nonvegetables]
def lol(eatables):
 for lk in eatables:
  if isinstance(lk,list):
   lol(lk)
  else :
   print(lk)