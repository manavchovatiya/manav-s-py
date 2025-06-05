numbers = [5,-9,36,12,18]
n =  len(numbers)
for i in range(n-1):
   swapped = False 
   for j in range(n-i-1):
       if numbers[j]>numbers[j+1]:
          numbers[j],numbers[j+1]=numbers[j+1],numbers[j]
          swapped = True 
   if not swapped:
      break
print(" Sorted list:")
for num in numbers:
   print(num)