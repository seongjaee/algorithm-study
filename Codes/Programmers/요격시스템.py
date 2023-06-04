def solution(targets):
    answer = 0
    targets.sort()
    while targets:
        cur_s, cur_e = targets.pop()
        answer += 1
        while targets:
            nxt_s, nxt_e = targets[-1]
            if nxt_e > cur_s:
                targets.pop()
            else:
                break
    
    return answer