import numpy as np


def handle_raw_input(raw_input):
    lines = raw_input.splitlines()
    dna_sequence = lines[0]
    cg_content_list = list(lines[1].split(" "))

    return dna_sequence, cg_content_list


def probability_match_string(dna_sequence, cg_content):
    c_probability = g_probability = float(cg_content) / 2
    a_probability = t_probability = (1 - float(cg_content)) / 2

    final_probability = 1
    for nucleotide in dna_sequence:
        match nucleotide:
            case _ if nucleotide in ["A", "T"]:
                final_probability *= a_probability
            case _ if nucleotide in ["C", "G"]:
                final_probability *= c_probability

    return np.log10(final_probability)


def calculate_list_probability(input_data):
    dna_sequence, cg_content_list = handle_raw_input(input_data)
    common_logarithm_list = []
    for cg_content in cg_content_list:
        common_logarithm = probability_match_string(dna_sequence, cg_content)
        if common_logarithm:
            common_logarithm_list.append(common_logarithm)

    return common_logarithm_list


if __name__ == "__main__":
    raw_input = """TGATTTATCCCAGACGTGGCCCTCCGTGACGAAATCTCTATCATATCCTGCTCCGAGACTGTCGCGGGAGGGGCGTCAATCACTTAACGTCCT
0.056 0.114 0.164 0.247 0.281 0.311 0.367 0.432 0.461 0.503 0.559 0.609 0.688 0.721 0.762 0.804 0.880 0.924"""
    result = calculate_list_probability(raw_input)
    print(' '.join(map(str, result)))
