def matching_characters(char1: str, char2: str, char1_index: int, char2_index: int, max_matching_distance: int) -> bool:
    assert len(char1) == len(char2) == 1, "char1 and char2 must be strings of size 1"

    chars_distance: int = char1_index - char2_index
    # module of distance
    if chars_distance < 0:
        chars_distance *= -1

    return char1 == char2 and chars_distance <= max_matching_distance

def jaro(s1: str, s2: str):
    s1_size: int = len(s1)
    s2_size: int = len(s2)

    max_matching_distance: int = int(max(s1_size, s2_size) / 2) - 1

    # amount of matching characters
    m: int = 0
    # amount of transpositions
    t: int = 0

    for i in range(s1_size):
        for j in range(s2_size):
            if matching_characters(s1[i], s2[j], i, j, max_matching_distance):
                m += 1

                # if the characters match but dont have the same index
                if i != j:
                    t += 1

    t /= 2

    sim_j: float = 0
    if m != 0:
        sim_j = ((m / s1_size) + (m / s2_size) + ((m - t) / m)) / 3

    return sim_j

def common_prefix(s1: str, s2: str):
    prefix_length = 0

    for i in range(4):
        if len(s1) == i or len(s2) == i or s1[i] != s2[i]:
            return prefix_length
        prefix_length += 1

    return prefix_length

def jaro_winkler(s1: str, s2: str):
    sim_j = jaro(s1, s2)

    # length of common prefix
    l = common_prefix(s1, s2)
    p = 0.1

    sim_w = sim_j + ( l * p * (1 - sim_j))

    return sim_w
