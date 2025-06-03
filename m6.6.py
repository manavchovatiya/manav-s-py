n=int(input("HOw many elements?"))
print(f"enter{n} elements below:")
numbers = [int(input()) for _ in range(n)]
numbers.sort(reverse=True)
print("Sorted list in descending order:")
for num in numbers:
   print(num)