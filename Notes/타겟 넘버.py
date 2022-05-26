def sol(numbers, m):
    if numbers == []:
        if m == 0:
            return 1
        else:
            return 0
    else:
        return sol(numbers[1:], m+numbers[0]) + sol(numbers[1:], m-numbers[0])

m = int(input())
n = int(input())

if n==0:
    print(0)
    
else:
    numbers = list(map(int, input().split()))
    print(sol(numbers, m))