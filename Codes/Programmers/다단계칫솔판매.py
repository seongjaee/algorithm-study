def solution(enroll, referral, seller, amount):
    def get_money(name, price):
        if name == "-":
            return
        fee = price // 10
        account[name] += price - fee
        if fee:
            get_money(parent[name], fee)

    parent = {name: referral[idx] for idx, name in enumerate(enroll)}
    account = {name: 0 for name in [*enroll, "-"]}

    for name, price in zip(seller, amount):
        get_money(name, price * 100)

    return [account[name] for name in enroll]
