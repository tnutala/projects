def gcd(x,y):

    divisors=[]
    if type(x)== int and type(y)==int:
        z = min(x,y)
        for i in range(1,z+1):
            if x%i==0 and y%i == 0:
                divisors.append(i)
            else:
                continue

    else:
        print("why are you putting non integer entries in a gcd script?")
    return "the gcd is "+str(max(divisors))
        
Input1=input("input first number:")
Input2=input("input first number:")
print gcd(Input1,Input2)
