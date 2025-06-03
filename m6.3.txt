n=int(input("How many elements ?"))
print(f" Enter {n} elements:")
numbers = [int(input()) for _ in range(n)]
even = sum(1 for num in numbers if num%2==0)
odd=n-even
print("Even numbers:",even)
print("Odd numbers:",odd)