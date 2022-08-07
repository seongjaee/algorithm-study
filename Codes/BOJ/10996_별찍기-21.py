def solution(k):
    if k == 1:
        print("*")
        return
    for i in range(2 * k):
        if i % 2 == 0:
            print(" ".join(["*"] * ((k + 1) // 2)))
        else:
            print(" " + " ".join(["*"] * (k // 2)))


n = int(input())
solution(n)
