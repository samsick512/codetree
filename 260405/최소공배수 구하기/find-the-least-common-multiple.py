import math
n, m = map(int, input().split())

def print_lcm(n,m):
    gcd = math.gcd(n,m)
    lcm =(n*m) //gcd

    print(lcm)
print_lcm(n,m)