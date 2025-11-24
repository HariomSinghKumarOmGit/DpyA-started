def fact(n):
    # base is 0 factorial
    if n == 0 or n == 1:
        return n
    #  recoursion 
    return n*fact(n-1)

print (fact(5))