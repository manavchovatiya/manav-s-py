n=int(input("Enter the number:"))
sum_odd=0
while n>0:
  digit=n%10
  if digit % 2!=0:
    sum_odd+=digit
  n=n//10
print("Addition of odd digits=",sum_odd)
