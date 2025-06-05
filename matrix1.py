print("  Enter 3x3 matrix A:")
matrix =  [[int(input()) for _ in range(3)] for _ in range(3)]
pos = sum(1 for row in matrix for num in row if num>0)
neg = sum(1 for row in matrix for num in row if num<0)
zero = 9-pos-neg
print(" Positive Numbers:",pos)
print("Negative Numbers :",neg)
print("Zeroes :",zero)