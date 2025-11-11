"""
N: number of AaBb organisms
k: the k-th generation
Each organism always mates with another AaBb organism and have two children.
The probability that an organism is heterozygous for both genes (AaBb) is 0.25
The probability that an organism is not heterozygous for both genes is 0.75
"""

from math import comb


def calculate_independent_alleles_probability(k, N):
    total_children = 2**k
    heterozygous_children_probability = 0.25
    not_heterozygous_children_probability = 0.75

    total_probability = 0

    for i in range(N, total_children + 1):
        total_combinations = comb(total_children, i)
        probability_i_heterozygous = (heterozygous_children_probability ** i) * (not_heterozygous_children_probability ** (total_children - i)) * total_combinations
        total_probability += probability_i_heterozygous

    return total_probability


if __name__ == "__main__":
    k = 5
    N = 7
    result = calculate_independent_alleles_probability(k, N)
    print(result)
