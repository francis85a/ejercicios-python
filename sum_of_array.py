def repeats(items):
    sum_singles = 0
    for item in items:
        if items.count(item) == 1:
            sum_singles += item
    return sum_singles