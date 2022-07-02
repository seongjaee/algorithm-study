import sys

input = sys.stdin.readline


def solution(s, t):
    s_without_b = ""
    t_without_b = ""
    for i in range(n):
        if s[i] != "b":
            s_without_b += s[i]
        if t[i] != "b":
            t_without_b += t[i]

    if s_without_b != t_without_b:
        return "NO"

    sai = []
    sci = []
    tai = []
    tci = []
    sbcnt = 0
    tbcnt = 0
    for i in range(n):
        if s[i] == "a":
            sai.append(i)
        elif s[i] == "c":
            sci.append(i)
        if t[i] == "a":
            tai.append(i)
        elif t[i] == "c":
            tci.append(i)

    for i in range(len(sai)):
        if sai[i] > tai[i]:
            return "NO"

    for i in range(len(sci)):
        if sci[i] < tci[i]:
            return "NO"

    return "YES"


q = int(input())
for _ in range(q):
    n = int(input())
    s = input().rstrip()
    t = input().rstrip()
    print(solution(s, t))
