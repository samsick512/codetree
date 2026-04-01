n, m = map(int, input().split())

def lcm(n,m):
    num =0
    for i in range(1,101):
        if i % n == 0 and i % m == 0 : 
            num = i
            break
    print(num)
lcm(n,m)