def pairs_contain(pairs_string):
    ranges = get_ranges(pairs_string)
    return (contain(ranges[0], ranges[1])) or (contain(ranges[1], ranges[0]))


def contain(range_a, range_b):
    return int(range_a[0]) <= int(range_b[0]) and int(range_a[1]) >= int(range_b[1])


def num_of_contained_pairs(pairs_string):
    return pairs_template(pairs_string, pairs_contain)


def num_of_overlap_pairs(pairs_string):
    return pairs_template(pairs_string, pairs_overlap)


def pairs_template(pairs_string, pair_func):
    hits = 0
    for line in pairs_string.split('\n'):
        if pair_func(line):
            hits += 1
    return hits


def pairs_overlap(pair_string):
    ranges = get_ranges(pair_string)
    if greater_or_equal_than(ranges[0][0], ranges[1][0]):
        temp = ranges[0]
        ranges[0] = ranges[1]
        ranges[1] = temp
    return greater_or_equal_than(ranges[0][1], ranges[1][0])

def greater_or_equal_than(a, b):
    return int(a) >= int(b)

def get_ranges(pair_string):
    pairs = pair_string.split(',')
    ranges = []
    for pair in pairs:
        ranges.append(pair.split('-'))
    return ranges
