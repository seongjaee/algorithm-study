from bisect import bisect_left

lang = ["java", "python", "cpp", "-"]
job = ["backend", "frontend", "-"]
career = ["junior", "senior", "-"]
food = ["chicken", "pizza", "-"]


def solution(info, query):
    answer = []
    all_query = {
        l: {j: {c: {f: [] for f in food} for c in career} for j in job} for l in lang
    }
    for row in info:
        l, j, c, f, score = row.split(" ")
        for w in [l, "-"]:
            for x in [j, "-"]:
                for y in [c, "-"]:
                    for z in [f, "-"]:
                        all_query[w][x][y][z].append(int(score))

    for l in lang:
        for j in job:
            for c in career:
                for f in food:
                    all_query[l][j][c][f].sort()

    for q in query:
        temp = q.split(" and ")
        l, j, c = temp[:-1]
        f, score = temp[-1].split(" ")
        score_list = all_query[l][j][c][f]
        idx = bisect_left(score_list, int(score))
        answer.append(len(score_list) - idx)

    return answer
