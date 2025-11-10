def cal_dominant_phenotype_probability(homozygous_dominant, heterozygous, homozygous_recessive):
    total_organism = homozygous_dominant + heterozygous + homozygous_recessive

    total_allele_count = 2 * total_organism
    recessive_allele_count = (2 * homozygous_recessive) + heterozygous

    reseesive_homozygous_probability = (recessive_allele_count / total_allele_count) * (
        (recessive_allele_count - 1) / (total_allele_count - 1))
    dominant_phenotype_probability = 1 - reseesive_homozygous_probability

    return dominant_phenotype_probability


print(cal_dominant_phenotype_probability(23, 26, 15))
