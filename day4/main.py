def pairs_contain(pairs_string):
    pairs = pairs_string.split(',')
    ranges = []
    for pair in pairs:
        ranges.append(pair.split('-'))
    return (contain(ranges[0], ranges[1])) or (contain(ranges[1], ranges[0]))


def contain(range_a, range_b):
    return int(range_a[0]) <= int(range_b[0]) and int(range_a[1]) >= int(range_b[1])


def num_of_contained_pairs(pairs_string):
    contained_pairs = 0
    for line in pairs_string.split('\n'):
        if pairs_contain(line):
            contained_pairs += 1
    return contained_pairs
