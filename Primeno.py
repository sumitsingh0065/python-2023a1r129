import math,sys,random

def is_prime(n):
    if n<2: return False
    if n%2==0: return n==2
    r=int(math.isqrt(n))
    for i in range(3,r+1,2):
        if n%i==0: return False
    return True

def fibonacci(n):
    a,b=0,1
    for _ in range(n):
        a,b=b,a+b
    return a

def gcd(a,b):
    while b:
        a,b=b,a%b
    return abs(a)

def stats(nums):
    n=len(nums)
    s=sum(nums)
    mean=s/n if n else 0
    nums_sorted=sorted(nums)
    mid=n//2
    med=(nums_sorted[mid] if n%2==1 else (nums_sorted[mid-1]+nums_sorted[mid])/2) if n else 0
    return {"count":n,"sum":s,"mean":mean,"median":med,"min":min(nums) if nums else None,"max":max(nums) if nums else None}

def parse_numbers(s):
    return [float(x) for x in s.replace(',', ' ').split()]

def menu():
    print("1) Prime check  2) Fibonacci  3) GCD  4) Stats  5) Random sample  0) Exit")
    return input("choice: ").strip()

def main():
    while True:
        c=menu()
        if c=='0': break
        if c=='1':
            n=int(input("n: "))
            print("prime" if is_prime(n) else "composite")
        elif c=='2':
            n=int(input("n: "))
            print(fibonacci(n))
        elif c=='3':
            a=int(input("a: ")); b=int(input("b: "))
            print(gcd(a,b))
        elif c=='4':
            s=input("numbers (space or comma separated): ")
            nums=parse_numbers(s)
            print(stats(nums))
        elif c=='5':
            s=input("numbers (space or comma separated): ")
            k=int(input("sample size: "))
            arr=parse_numbers(s)
            print(random.sample(arr, min(k,len(arr))))
        else:
            print("invalid choice")

if __name__=="__main__":
    try:
        main()
    except (EOFError,KeyboardInterrupt):
        sys.exit(0)
