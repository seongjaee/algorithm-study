def solution(relation):
    answer = 0
    row_num = len(relation)
    col_num = len(relation[0])
    
    # 유일한 키인지 확인
    def check_unique(keys):
        temp = set()
        for i in range(row_num):
            now = []
            for key in keys:
                now.append(relation[i][key])
            temp.add(tuple(now))
            
        return row_num == len(temp)
    
    
    # 유일한 키들 찾기
    uniqueness_keys = []
    for i in range(1, 1 << col_num):
        now = set()
        for j in range(col_num):
            if i & (1 << j):
                now.add(j)
        if check_unique(now):
            uniqueness_keys.append(now)
            
    uniqueness_keys.sort(key=lambda arr: len(arr))
    
    # 유일한 키들 중 최소성을 만족하는 키 찾기
    candidate_keys = []
    for key in uniqueness_keys:
        flag = True
        for candidate in candidate_keys:
            if set(candidate).issubset(key):  # 후보키를 포함하는 키는 최소성 만족 X
                flag = False
                break
        if flag:
            candidate_keys.append(key)
                    
    return len(candidate_keys)