print(" Enter 3x3 matrix A:")
a = [[int(input()) for _ in range(3)] for _ in range(3)]
print(" Enter 3x3 matrix B :")
b = [[int(input()) for _ in range(3)] for _ in range(3)]
c = [[a[i][j] + b[i][j] for j in range(3) ]for i in range(3)]
print(" Resiltant Matrix C:")
for row in c:
     print('\t'.join(map(str,row)))