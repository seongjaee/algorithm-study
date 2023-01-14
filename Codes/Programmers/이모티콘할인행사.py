from itertools import product


def solution(users, emoticons):
    n = len(users)
    m = len(emoticons)

    max_result = [0, 0]

    def shopping_cart(user_idx, discounts):
        total_buy_price = 0
        sale_cut, price_cut = users[user_idx]
        for emoticion_price, discount in zip(emoticons, discounts):
            price = emoticion_price * (100 - discount) // 100
            if discount >= sale_cut:
                total_buy_price += price
            if total_buy_price >= price_cut:
                return [1, 0]

        return [0, total_buy_price]

    all_cases = product([10, 20, 30, 40], repeat=m)
    for discounts in all_cases:
        result = [0, 0]
        for i in range(n):
            plus_cnt, price = shopping_cart(i, discounts)
            result[0] += plus_cnt
            result[1] += price
        if result[0] > max_result[0]:
            max_result = result
        elif result[0] == max_result[0] and result[1] > max_result[1]:
            max_result = result

    return max_result


users = [[40, 10000], [25, 10000]]
emoticons = [7000, 9000]


# users = [
#     [40, 2900],
#     [23, 10000],
#     [11, 5200],
#     [5, 5900],
#     [40, 3100],
#     [27, 9200],
#     [32, 6900],
# ]
# emoticons = [1300, 1500, 1600, 4900]


print(solution(users, emoticons))
