num=int (input(" Enter a number:"))
temp=num
sum_digits=0
mul_digits=1
while temp>0:
   digits=temp%10
   sum_digits += digits
   mul_digits *= digits
   temp=temp//10
if mul_digits==sum_digits:
   print("perfect")
else:
   print("Not perfect")