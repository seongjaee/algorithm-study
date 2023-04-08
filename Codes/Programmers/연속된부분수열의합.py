def solution(sequence, k):
    answer = []
    presum = [0]
    for num in sequence:
        presum.append(presum[-1] + num)
        
    min_length = len(sequence) + 1
    l, r = 0, 1
    now = 0
    while r < len(presum) and r - l <= min_length:        
        if presum[r] - presum[l] == k:
            if r - l < min_length:
                min_length = r - l
                answer = [l, r - 1]
            l += 1
        elif presum[r] - presum[l] >= k:
            l += 1
        else:
            r += 1
            
    return answer