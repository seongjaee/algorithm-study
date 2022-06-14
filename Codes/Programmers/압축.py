def solution(msg):
    answer = []
    word = {chr(i + 64): i for i in range(1, 27)}
    now_index = 27

    i = 0
    now_word = ""
    while i < len(msg):
        nxt_word = now_word + msg[i]
        if nxt_word not in word:
            answer.append(word[now_word])
            word[nxt_word] = now_index
            now_index += 1
            now_word = ""
        else:
            now_word = nxt_word
            i += 1

    answer.append(word[now_word])

    return answer
