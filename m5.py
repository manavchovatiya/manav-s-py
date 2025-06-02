print(" mark grade ")
print("100-80 Distincion ")
print("60-79 First class")
print("36-59 Second class")
print("0-39 fail")



m=int(input(" Enter marks:"))
if m>=80 and m<=100:
   print("distinction")
elif m>=60 and m<80:
   print(" First class")
elif m>=35 and m<60:
  print("second class")
elif m>=0 and m<35:
  print("Fail")
else:
  print(" invalid marks")
print(" Have a nice day")