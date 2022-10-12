from math import gcd
import sys

input = sys.stdin.readline

n, m = map(int, input().split(":"))
g = gcd(n, m)

print(f"{n//g}:{m//g}")
