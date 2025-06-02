num=int(input("Enter a number:"))
last=num%10
while num>9:
 num=num//10
first=num
sum_fl=first+last
print("sum of first and last digits:",sum_fl)
