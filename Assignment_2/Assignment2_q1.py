# Write a function to return simple interest

def simple_interest(P,R,T):
    SI = (P * R * T)/100
    return SI
      
P=int(input("Enter principal amount"))
R=int(input("Enter rate of interest"))
T=int(input("Enter time period"))

print('The Simple Interest is', simple_interest(P, R, T))

