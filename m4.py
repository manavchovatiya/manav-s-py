a,b,c=map(int,input(" Enter three numbers:").split())
if a>b:
   if a>c:
      print(a,"is max")
   else:
      print(c,"is max")
elif b>c:
  print(b,"is max")
else:
  print(c,"is max")