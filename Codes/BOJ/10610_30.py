def solution(numbers):
    if 0 not in numbers:
        print(-1)
        return
    if sum(numbers) % 3 != 0:
        print(-1)
        return

    print(''.join(map(str, sorted(numbers, reverse=True))))
    return

numbers = list(map(int,list(input())))
solution(numbers)