a, b, c = map(int, input().split())

def print_num(a,b,c):
    min_val = a
    if (a>b):
        min_val = b
    if (a>c):
        min_val = c
    return min_val
print(print_num(a,b,c))        