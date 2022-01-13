from jaro_winkler_alg import jaro_winkler

# MARTHA, MARHTA: 96
# DIXON, DICKSONX: 74
# JELLYFISH, SMELLYFISH: 88
# CRATE, TRACE: 73

examples = [
    ["MARTHA", "MARHTA", 0.9611111111111111],
    ["DIXON", "DICKSONX", 0.7466666666666666],
    ["JELLYFISH", "SMELLYFISH", 0.8870370370370372],
    ["CRATE", "TRACE", 0.7333333333333334]
]

for example in examples:
    word_1, word_2, sim_w = example
    print("TESTER: ", jaro_winkler(word_1, word_2))
    print("RESULT: ", sim_w)
    assert jaro_winkler(word_1, word_2) == sim_w