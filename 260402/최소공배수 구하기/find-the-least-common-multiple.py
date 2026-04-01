n, m = map(int, input().split())

def lcm(n,m):
    for i in range(min(n,m),0,-1):
        if n % i ==0 and m % i ==0:
            gcd = i
            break
    return n*m // gcd
print(lcm(n,m))