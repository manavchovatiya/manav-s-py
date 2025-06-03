n=int(input("How many elements?"))
print(f" Enter {n} elements below:")
numbers = [int(input()) for _ in range(n)]
numbers.sort()
print(" Sorted list:")
print(' '.join(map(str,numbers)))