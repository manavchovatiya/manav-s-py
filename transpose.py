n= int(input("Enter n:"))
print(f"Enter {n}x{n} matrix:")
matrix = [[int(input()) for _ in range(n)] for _ in range(n)]
print(" Original matrix:")
for row in matrix:
   print('\t'.join(map(str,row)))
print("Transpose matrix:")
for i in range(n):
   print('\t'.join(str(matrix[j][i]) for j in range(n)))
