def collaz(start):
    result = [start]
    now = start
    while now != 1:
        if now % 2:
            now = now * 3 + 1
        else:
            now //= 2
        result.append(now)
        
    return result
            
def get_area_trapezoid(a, b):
    return 0.5 * (a + b)

def solution(k, ranges):
    answer = []
    series = collaz(k)
    n = len(series)
    areas = []
    for i in range(n - 1):
        areas.append(get_area_trapezoid(series[i], series[i + 1]))
        
    presum = [0]
    for i in range(n - 1):
        presum.append(presum[-1] + areas[i])
    
    for s, e in ranges:
        if s > n - 1 + e:
            answer.append(-1)
            continue
        
        result = presum[n - 1 + e] - presum[s]
        answer.append(presum[n - 1 + e] - presum[s])

    return answer