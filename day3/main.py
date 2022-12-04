def rucksack(sacks):
    total = 0
    for sack in sacks.split():
        total += char_score(common_item(sack))
    return total


def common_item(sack):
    length = len(sack)
    halfpoint = int(length / 2)
    sack1 = sack[0:halfpoint]
    sack2 = sack[halfpoint:length + 1]
    sack_set = set(sack2)
    for ch in sack1:
        if ch in sack_set:
            return ch
    return False


def find_badge(sack_arr):
    s1 = set(sack_arr[0])
    s2 = set(sack_arr[1])
    s3 = set(sack_arr[2])
    intersection = s1.intersection(s2.intersection(s3))
    for i in intersection:
        return i
    return False


def char_score(ch):
    unicode = ord(ch)
    uni_a_lower = ord('a')
    if uni_a_lower <= unicode <= ord('z'):
        return unicode - uni_a_lower + 1
    uni_a_upper = ord('A')
    if uni_a_upper <= unicode <= ord('Z'):
        return unicode - uni_a_upper + 27
    return False


def badge_score(sacks):
    sack_list = sacks.split()
    if len(sack_list) % 3 != 0:
        return False

    score = 0
    i = 0
    while i < len(sack_list):
        score += char_score(find_badge(sack_list[i: i + 3]))
        i += 3
    return score
