import sys

lines = sys.stdin.readlines()

taunt_cnt = 0
exp_cnt = [0] * 11


def taunt():
    global taunt_cnt
    k = exp_cnt[0]
    exp_cnt[0] = (exp_cnt[0] + 1) % 4
    taunt_cnt += 1
    if k == 0:
        return sentence().capitalize()
    elif k == 1:
        return f"{taunt()} {sentence().capitalize()}"
    elif k == 2:
        return f"{noun().capitalize()}!"
    elif k == 3:
        return sentence().capitalize()


def sentence():
    k = exp_cnt[1]
    exp_cnt[1] = (exp_cnt[1] + 1) % 3
    if k == 0:
        return f"{past_rel()} {noun_phrase()}"
    elif k == 1:
        return f"{present_rel()} {noun_phrase()}"
    elif k == 2:
        return f"{past_rel()} {article()} {noun()}"


def noun_phrase():
    return f"{article()} {modified_noun()}"


def modified_noun():
    k = exp_cnt[2]
    exp_cnt[2] = (exp_cnt[2] + 1) % 2
    if k == 0:
        return noun()
    elif k == 1:
        return f"{modifier()} {noun()}"


def modifier():
    k = exp_cnt[3]
    exp_cnt[3] = (exp_cnt[3] + 1) % 2
    if k == 0:
        return adjective()
    elif k == 1:
        return f"{adverb()} {adjective()}"


def present_rel():
    return f"your {present_person()} {present_verb()}"


def past_rel():
    return f"your {past_person()} {past_verb()}"


def present_person():
    k = exp_cnt[4]
    exp_cnt[4] = (exp_cnt[4] + 1) % 3
    return present_people[k]


def past_person():
    k = exp_cnt[5]
    exp_cnt[5] = (exp_cnt[5] + 1) % 5
    return past_people[k]


def noun():
    k = exp_cnt[6]
    exp_cnt[6] = (exp_cnt[6] + 1) % 11
    return nouns[k]


def present_verb():
    k = exp_cnt[7]
    exp_cnt[7] = (exp_cnt[7] + 1) % 2
    return present_verbs[k]


def past_verb():
    k = exp_cnt[8]
    exp_cnt[8] = (exp_cnt[8] + 1) % 2
    return past_verbs[k]


def article():
    return "a"


def adjective():
    k = exp_cnt[9]
    exp_cnt[9] = (exp_cnt[9] + 1) % 7
    return adjs[k]


def adverb():
    k = exp_cnt[10]
    exp_cnt[10] = (exp_cnt[10] + 1) % 5
    return advs[k]


def has_alpha(word):
    for char in word:
        if char.isalpha():
            return True
    return False


def is_exception(string):
    theholygrail = "theholygrail"
    cnt = 0
    for char in string:
        if char == theholygrail[cnt]:
            cnt += 1
        if cnt == len(theholygrail):
            return True
    return False


present_people = ["steed", "king", "first-born"]
past_people = ["mother", "father", "grandmother", "grandfather", "godfather"]
nouns = [
    "hamster",
    "coconut",
    "duck",
    "herring",
    "newt",
    "peril",
    "chicken",
    "vole",
    "parrot",
    "mouse",
    "twit",
]
present_verbs = ["is", "masquerades as"]
past_verbs = ["was", "personified"]
adjs = [
    "silly",
    "wicked",
    "sordid",
    "naughty",
    "repulsive",
    "malodorous",
    "ill-tempered",
]
advs = [
    "conspicuously",
    "categorically",
    "positively",
    "cruelly",
    "incontrovertibly",
]

answer = []

for line in lines:
    result = []
    knight_words = line.split()
    result.append(f'Knight: {" ".join(knight_words)}')

    n = 0
    for word in knight_words:
        if has_alpha(word):
            n += 1

    q, r = divmod(n, 3)
    m = q + (1 if r else 0)

    if is_exception("".join(knight_words).lower()):
        result.append(f"Taunter: (A childish hand gesture).")
        m -= 1

    while taunt_cnt < m:
        result.append(f"Taunter: {taunt()}.")

    taunt_cnt = 0
    answer.append("\n".join(result))

print("\n\n".join(answer))
