import sys

input = sys.stdin.readline

while True:
    try:
        x = int(input()) * 10000000
        n = int(input())
        numbers = []
        for _ in range(n):
            num = int(input())
            if num < x:
                numbers.append(num)

        numbers.sort()
        left = 0
        right = len(numbers) - 1
        while left < right:
            if numbers[left] + numbers[right] == x:
                print(f"yes {numbers[left]} {numbers[right]}")
                break
            elif numbers[left] + numbers[right] > x:
                right -= 1
            else:
                left += 1
        else:
            print(f"danger")

    except:
        break
