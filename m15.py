n=int(input("1^2+2^2+3^2+4^2+....+n^2 Enter n:"))
sum_series=sum(i*i for i in range(1,n+1))
print("sum=",sum_series)