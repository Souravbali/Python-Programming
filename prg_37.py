def pow(a,b):
    if (b==0):
        return 1 
    return a * pow(a,b-1)
n  = int(input())
m = int(input())
print(pow(n,m))