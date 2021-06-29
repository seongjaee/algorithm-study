def power(a, k):
    ans = 1
    while k >0:
        if k%2 ==1:
            ans *= a
        a *= a
        k //= 2
    return ans