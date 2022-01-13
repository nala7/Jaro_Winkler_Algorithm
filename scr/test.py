from jaro_winkler_alg import jaro_winkler

# MARTHA, MARHTA: 94
# DIXON, DICKSONX: 76
# JELLYFISH, SMELLYFISH: 89

examples = [
    ["MARTHA", "MARHTA", 0.94],
    ["DIXON", "DICKSONX", 0.76],
    ["JELLYFISH", "SMELLYFISH", 0.89],
    ["CRATE", "TRACE", 0.73]

]

for example in examples:
    word_1, word_2, sim_w = example
    print("TESTER: ", jaro_winkler(word_1, word_2))
    print("RESULT: ", sim_w)
    # assert jaro_winkler(word_1, word_2) == sim_w