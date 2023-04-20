#numbers.py
'''Different Predefined Numbers'''
#functions

def length(n):
    '''Returns length of number'''
    n=int(n)
    c=0
    while n>0:
        c+=1
        n//=10
    return c

def isPallindrom(n):
    '''Checks pallindrom or not'''
    n=int(n)
    x=n
    s=0
    while x>0:
        s=s*10+x%10
        x//=10
    return s==n

def isSpecial(n):
    '''Checks special number or not'''
    n=int(n)
    x=n
    s=0
    while x>0:
        d=x%10
        s=s+factorial(d)
        x//=10
    return s==n

def isKrishnamurthy(n):
    '''Checks krishnamurthy number or not'''
    return isSpecial(n)

def isArmstrong(n):
    '''Checks armstrong number or not'''
    n=int(n)
    x=n
    s=0
    l=length(n)
    while x>0:
        d=x%10
        s=s+d**l
        x//=10
    return s==n

def factorial(n):
    '''Returns factorial of given number'''
    n=int(n)
    f=1
    for i in range(1,n+1):
        f*=i
    return f

def isAutomorphic(n):
    '''Checks automorphic number or not'''
    n=int(n)
    l=length(n)
    return n==(n*n)%(10**l)

def isKaprekar(n):
    '''Checks kaprekar number or not'''
    n=int(n)
    l=10**length(n)
    p=n*n
    return n==p%l+p//l

def sumDigits(n):
    '''Returns sum of digits'''
    n=int(n)
    s=0
    while n>0:
        s+=n%10
        n//=10
    return s

def productDigits(n):
    '''Returns product of digits'''
    n=int(n)
    p=1
    while n>0:
        p*=n%10
        n//=10
    return p

def isMagic(n):
    '''Checks magic number or not'''
    while n>9:
        n=sumDigits(n)
    return n==1

def numFactors(n):
    '''Counts Number of Factors'''
    n=int(n)
    c=0
    i=1
    j=n
    while i<j:
        j=n//i
        if n%i==0:
            c+=(1 if i==j else 2)
        i+=1
    return c

def factors(n):
    '''Returns factors as a lsit'''
    n=int(n)
    c=[]
    i=1
    j=n
    while i<j:
        j=n//i
        if n%i==0:
            c.append(i)
            if(i!=j):
                c.append(j)
        i+=1
    c.sort()
    return c
def sumFactors(n):
    '''Returns sum of factors'''
    return sum(factors(n))

def isPerfect(n):
    '''Checks a number is perfect number or not'''
    return n*2==sumFactors(n)

def isPrime(n):
    '''Checks prime number or not'''
    return numFactors(n)==2

def isPerfectSquare(n):
    '''Checks number is perfect square or not'''
    return numFactors(n)%2==1

def isPerfectCube(n):
    '''Checks number is perfect cube or not'''
    n=int(n)
    i=1
    while i**3<n:
        i+=1
    return i**3==n

def isSunny(n):
    '''Checks number is sunny number or not'''
    return isPerfectSquare(n+1)

def isVampire(n):
    '''Checks number is vampire number or not'''
    n=int(n)
    l=length(n)//2-1
    i=10**l
    j=n//i
    c=list(str(n))
    c.sort()
    while i<=j:
        if n%i==0:
            cf=list(str(i))
            cf.extend(list(str(j)))
            cf.sort()
            if c==cf:
                return True
        i+=1
        j=n//i
    return False

def primeFactorize(n):
    '''Returns prime factorized factors'''
    n=int(n)
    p=2
    x=1
    f=[]
    while n>1:
        if n%p==0:
            f.append(p)
            n/=p
        else:
            p+=x
            x=2
    return f

def isSmith(n):
    '''Checks wheather a number is smith or not'''
    if isPrime(n):
        return False
    f=primeFactorize(n)
    s=0
    for i in f:
        s+=sumDigits(i)
    return s==sumDigits(n)

def isTriangular(n):
    '''Checks a number is triangular number or not'''
    n=int(n)
    i=1
    s=0
    while s<n:
        s+=i
        i+=1
    return s==n

def triangularSeries(n):
    '''Returns triangular series'''
    r=[]
    n=int(n)
    s=0
    for i in range(1,n+1):
        s+=i
        r.append(s)
    return r

def isFibonacci(n):
    '''Checks number is fibonacci or not'''
    n=int(n)
    a=1
    b=0
    c=0
    while c<n:
        c=a+b
        a=b
        b=c
    return c==n

def fibonacciSeries(n):
    '''Returns fibonacci series'''
    n=int(n)
    a=1
    b=0
    c=[]
    for i in range(n):
        c.append(a+b)
        a=b
        b=c[i]
    return c

def isSpy(n):
    '''Checks number is spy or not'''
    return sumDigits(n)==productDigits(n)

def lcm(a):
    '''Returns lcm'''
    a=numify(a)
    m=max(a)
    i=m
    while True:
        for j in a:
            if i%j!=0:
                break
        else:
            return i
        i+=m

def hcf(a):
    '''Returns hcf'''
    a=numify(a)
    i=min(a)
    while True:
        for j in a:
            if j%i!=0:
                break
        else:
            return i
        i-=1

def numify(a):
    '''Converts each element to number in list'''
    l=[]
    for i in a:
        l.append(int(i))
    if type(a)==type(()):
        l=tuple(l)
    return l

def isFscinating(n):
    '''Checks number is fascinating or not'''
    n=int(n)
    for i in range(1,10):
        x=n
        c=0
        while x>0:
            if x%10==i:
                c+=1
            x//=10
        x=n*2
        while x>0:
            if x%10==i:
                c+=1
            x//=10
        x=n*3
        while x>0:
            if x%10==i:
                c+=1
            x//=10
        if c!=1:
            return False
    return True

def isBeautiful(n):
    '''Checks a number is beautiful or not'''
    n=int(n)
    for i in range(10):
        x=n
        c=0
        while x>0:
            if x%10==i:
                c+=1
            x//=10
        if c!=0 and c!=i:
            return False
    return True

def digitFrequency(n):
    '''Returns frequency of digits in number as dictionary'''
    f={}
    while n>0:
        d=n%10
        f[d]=(f[d] if d in f else 0)+1
        n//=10
    return f
