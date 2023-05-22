from collections import Counter


def is_twin(a, b):
    return Counter(a.lower()) == Counter(b.lower())
