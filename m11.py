for i in range(1,6):
   print(f" Enter three marks for student #{i}:",end=" ")
   marks=list(map(int,input().split()[:3]))
   average=sum(marks)//3
print("Average=",average)