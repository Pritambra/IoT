# write a function to return compound interest

def Amount(P,R,T):
    A = P * (pow((1 + R / 100), T))
    return A
      
P=int(input("Enter principal amount"))
R=int(input("Enter rate of interest"))
T=int(input("Enter time period"))
 

A = Amount(P, R, T)
print('The Amount is', A)

def Compound_Interest(A, P):
    CI = A - P
    return CI

print('The Compound interest is', Compound_Interest(A, P))

