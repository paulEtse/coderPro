import math


def calculate_total_price(prices, discount):
    higher = max(prices)
    return math.floor(sum(prices) - higher + higher * (1 - discount / 100))
