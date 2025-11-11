"""
Possible genotype combinations between two parents:
1. AA - AA
2. AA - Aa
3. AA - aa
4. Aa - Aa
5. Aa - aa
6. aa - aa
"""


def calculating_expected_offspring(couples_genotypes_1, couples_genotypes_2,
                                   couples_genotypes_3, couples_genotypes_4,
                                   couples_genotypes_5, couples_genotypes_6):
    expected_offspring = 2 * (
        couples_genotypes_1 * 1 +
        couples_genotypes_2 * 1 +
        couples_genotypes_3 * 1 +
        couples_genotypes_4 * 0.75 +
        couples_genotypes_5 * 0.5 +
        couples_genotypes_6 * 0
    )

    return expected_offspring


if __name__ == "__main__":
    # result = calculating_expected_offspring(1, 0, 0, 1, 0, 1)
    result = calculating_expected_offspring(19809, 16031, 16196, 19235, 16653, 17156)
    print(result)
