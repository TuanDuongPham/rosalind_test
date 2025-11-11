from P18_enumerating_gene_order import permute

"""
Since each position of a permutation is either positive or negative, the total set will be 2 ** n
Each set have n! combination
=> Therefore, total permutation will be n! * (2 ** n)
"""


def permute_signed(integers_list):
    unsigned_permutations = permute(integers_list)

    all_permutations = []
    for perm in unsigned_permutations:
        n = len(perm)
        for sign_mask in range(2 ** n):
            signed_perm = []
            for i in range(n):
                if sign_mask & (2 ** i):
                    signed_perm.append(-perm[i])
                else:
                    signed_perm.append(perm[i])
            all_permutations.append(signed_perm)
    return all_permutations


def enumering_signed_gene_order(n):
    first_n_integers = list(range(1, n + 1))
    return permute_signed(first_n_integers)


if __name__ == "__main__":
    n = 3
    permutations = enumering_signed_gene_order(n)
    print(len(permutations))
    for p in permutations:
        print(' '.join(map(str, p)))
