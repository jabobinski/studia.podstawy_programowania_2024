from itertools import permutations

def generate_permutations(input_list):
    return list(permutations(input_list))

a = [1, 2, 3]
permutations_list = generate_permutations(a)
print(permutations_list)