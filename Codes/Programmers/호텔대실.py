from heapq import heappop, heappush


def hhmm_to_num(hhmm):
    h, m = map(int, hhmm.split(":"))
    return h * 60 + m


def solution(book_time):
    answer = 0
    times = []
    for book in book_time:
        s, e = map(hhmm_to_num, book)
        times.append([s, e + 9])
    times.sort()
    end_time_heap = []
    for start, end in times:
        while end_time_heap:
            if start <= end_time_heap[0]:
                break
            heappop(end_time_heap)

        heappush(end_time_heap, end)
        answer = max(answer, len(end_time_heap))
    return answer
