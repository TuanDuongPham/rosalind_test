def calculate_partial_permutation(n, k):
    if k > n:
        return False

    total_partial_permmutation = 1
    for i in range(k):
        total_partial_permmutation *= (n - i)

    return total_partial_permmutation % 1000000


if __name__ == "__main__":
    n = 82
    k = 8
    print(calculate_partial_permutation(n, k))
