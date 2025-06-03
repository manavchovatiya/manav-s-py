n=int(input(" How many elements ? "))
print(f" Enter {n}elements:")
elements = [int(input()) for _ in range(n)]
print(" Maximum=",max(elements))
