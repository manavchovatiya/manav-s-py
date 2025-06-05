#Greatest common difference(GCD) using recursion(Euclid's Algorithm)

def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)
print("GCD of 166 and 16 is: ",gcd(166,16)) 
                                                                                                                                                                                                                                                                                                                                                                     