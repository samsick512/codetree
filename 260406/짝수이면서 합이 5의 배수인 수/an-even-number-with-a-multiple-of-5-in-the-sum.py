n = int(input())

def print_num(n):
    num = n /10
    mum = n //10
    if n/2:
        if (num+mum)//5==0:
            return print("Yes")
        else :
            return print("No")
print_num(n)