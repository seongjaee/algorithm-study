def calculate(order, arr):
    for o in order:
        nxt = []
        i = 0
        while i < len(arr):
            now = arr[i]
            if now == o:
                nxt.append(str(eval(nxt.pop() + now + arr[i+1])))
                i += 2
            else:
                nxt.append(now)
                i += 1
        arr = nxt
    return abs(int(arr.pop()))
        

def solution(expr):
    result = 0
    splited = ['']
    for e in expr:
        if e.isdigit():
            splited[-1] += e
        else:
            splited.append(e)
            splited.append('')
    
    all_orders = ['-*+', '-+*', '*-+', '+-*', '*+-', '+*-']
    
    for order in all_orders:
        result = max(calculate(order, splited), result)
        
    return result