DISTS = [2, 3, 4]

def solution(weights):
    answer = 0
    counter = {}
    for weight in weights:
        answer += counter.get(weight, 0)
        counter[weight] = counter.get(weight, 0) + 1
        
    torque = {}
    for weight, count in counter.items():
        for d in DISTS:
            nxt = weight * d
            answer += torque.get(nxt, 0) * count
            torque[nxt] = torque.get(nxt, 0) + count
        
    return answer