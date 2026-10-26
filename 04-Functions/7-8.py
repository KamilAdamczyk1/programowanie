def f(amount_to_pay):
    if amount_to_pay > 0:
        five_rest = amount_to_pay % 5
        five = amount_to_pay // 5
        two_rest = five_rest % 2
        two = five_rest // 2
