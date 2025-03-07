#fabonacci series by recursion
def fab(n):

    if(n==1):
        return (1)
    elif(n==0):
        return 0
    else:
       return fab(n-1)+fab(n-2)
print(fab(9))      
#fabonacci series
def series(term):
    if term <= 1:
        return term
    else: 
        return series(term-1) + series(term-2)

for i in range(3):  # Use the number of terms directly here
    print(series(i))

#factorial by recursion 
def fac(n):
    if n==1 or n==0 :
        return 1
    else:
        return n*fac(n-1)
print(fac(7))  

