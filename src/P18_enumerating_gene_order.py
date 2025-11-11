def permute(intergers_list):
    if len(intergers_list) == 1:
        return [intergers_list]

    permutations = []
    for i in range(len(intergers_list)):
        current = intergers_list[i]
        remaining = intergers_list[:i] + intergers_list[i+1:]
        for p in permute(remaining):
            permutations.append([current] + p)
    return permutations


def enumering_gene_order(n):
    first_n_integers = list(range(1, n + 1))
    return permute(first_n_integers)


if __name__ == "__main__":
    n = 5
    permutations = enumering_gene_order(n)
    print(len(permutations))
    for p in permutations:
        print(' '.join(map(str, p)))
