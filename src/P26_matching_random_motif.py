def handle_raw_input(raw_input):
    lines = raw_input.splitlines()
    line_1 = list(lines[0].split(' '))
    N_random_string = line_1[0]
    gc_content = line_1[1]
    dna_sequence = lines[1]

    return N_random_string, gc_content, dna_sequence


def matching_random_motif(N_random_strings, gc_content, dna_sequence):
    a_content = (1 - float(gc_content)) / 2
    g_content = float(gc_content) / 2

    probability_not_motif = 1
    for nucleotide in dna_sequence:
        match nucleotide:
            case _ if nucleotide in ["A", "T"]:
                probability_not_motif *= a_content
            case _ if nucleotide in ["C", "G"]:
                probability_not_motif *= g_content

    final_probability = 1 - ((1-probability_not_motif) ** float(N_random_strings))

    return final_probability


if __name__ == "__main__":
    raw_input = """98196 0.490220
AGCGAGCGG"""
    N_random_string, gc_content, dna_sequence = handle_raw_input(raw_input)
    print(matching_random_motif(N_random_string, gc_content, dna_sequence))
