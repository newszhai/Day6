def factorial(n):
    if n==1:
        return 1#边界
    else:
        return n*factorial(n-1)#递归函数


num = 10
result=factorial(num)
print(f"The factorial of {num} is:{result}")
#The factorial of 5 is:120
