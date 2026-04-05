n = int(input())

def print_num(n):
    sum =0
    for i in range(1, n + 1):
        sum += i
    return sum//10

print(print_num(n))