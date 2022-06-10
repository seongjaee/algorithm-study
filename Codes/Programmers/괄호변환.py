def check_right(balanced):
    stack = []
    for char in balanced:
        if char == '(':
            stack.append(char)
        else:
            try:
                stack.pop()
            except:
                return False
    if stack:
        return False
    return True


def separate(p):
    u, v = '', ''
    cnt = 0
    for idx, value in enumerate(p):
        if value == '(':
            cnt += 1 
        else:
            cnt -= 1
        u += value
        if cnt == 0:
            v = p[idx + 1:]
            break
            
    return u, v

def swap(u):
    temp = ''
    for char in u:
        if char == '(':
            temp += ')'
        else:
            temp += '('
    return temp
    

def solution(p):
    if p == '':
        return ''
    
    u, v = separate(p)
    
    if check_right(u):
        return u + solution(v)
        
    else:
        temp = '('
        temp += solution(v)
        temp += ')'
        u = u[1:-1]
        temp += swap(u)
        return temp