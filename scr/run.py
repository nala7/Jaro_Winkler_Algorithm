from jaro_winkler_alg import jaro_winkler

print("JARO-WINKLER DISTANCE ALGORITHM")
print("Please insert your first string and then press enter:")
str_1 = input()
print("Please insert your second string and then press enter:")
str_2 = input()

res = jaro_winkler(str_1, str_2)

print("Similarity was: ", res)