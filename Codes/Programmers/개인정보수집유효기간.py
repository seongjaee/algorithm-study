def time_to_num(date):
    year, month, day = map(int, date.split("."))
    return year * 12 * 28 + month * 28 + day


def solution(today, terms, privacies):
    today = time_to_num(today)
    answer = []
    term_dict = {}
    for term in terms:
        kind_term, month = term.split(" ")
        term_dict[kind_term] = int(month)

    for i, privacy in enumerate(privacies):
        date, term = privacy.split(" ")
        month = term_dict[term]
        deadline = time_to_num(date) + month * 28
        if today >= deadline:
            answer.append(i + 1)

    return answer
