from itertools import combinations_with_replacement

def solution(n, info):
    combs = list(combinations_with_replacement(range(10, -1, -1), n))
    max_value = 0
    max_c = []
    for c in combs:
        apeach = 0
        ryan = 0
        ryan_info = [0] * 11
        for i in c:
            ryan_info[i] += 1
        
        for i in range(11):
            score = 10 - i
            if info[i] == 0 and ryan_info[i] == 0:
                continue
            if info[i] >= ryan_info[i]:
                apeach += score
            else:
                ryan += score

        if max_value < ryan - apeach:
            max_value = ryan - apeach
            max_c = ryan_info

    if max_value:
        return max_c
    else:
        return [-1]

print(solution(5, [2,1,1,1,0,0,0,0,0,0,0]))