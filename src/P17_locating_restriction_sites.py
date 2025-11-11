# The reverse panlidrimes are seqences that have length of at least 4 and at most 12 => When replacing A with T, T with A, C with G and G with C, we get the same sequence when read backwards.

def locating_restriction_sites(dna_sequence):
    restriction_sites = []
    sequence_length = len(dna_sequence)

    for i in range(sequence_length):
        for length in range(4, 13):
            if i + length <= sequence_length:
                substring = dna_sequence[i:i + length]
                translate_dict = str.maketrans({'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'})
                new_substring = substring.translate(translate_dict)[::-1]

                if substring == new_substring:
                    restriction_sites.append((i + 1, length))

    return restriction_sites


if __name__ == "__main__":
    dna_sequence = """CGCGGCAGTCGCGAATGCTCCCATGTAGGTAACTGTTCTATTGGGCCTTAATTAGCCCCAACCATACGTGGGAAGTACAATTGACCCAACCGAGGCTAATTGAACACATGGTCACGCTCGGGAGGACCGACCGTACCGTCTTGTAAAGCTGCGGCGTTAGCCATGGCATACACTGTTCGGGAACCTGAAGATGCACTCCCAAAGCAAAACCCCCCTTCCCGTCTGCCCCCGCGTCCCAAGATGGACACCAGCAGAGCAGCTGGTTACCGAACTTTTCGGCTGTCCAAGCCATCCCAATATATAAGTCGACTTCCGCTCCGCCTTACATAGTCGGCCGTAATCATCCAACTTTCTATTACTCGTCATGTATACAGCTGCAGTGTTAGTGACGAGTACTGTGCAAAACCCATGGGTTAGAATGCGTAACTCCAACACCACAGAAAAGAGTTACAGTTGGTACCAATTGGCGGAGCGACCGATAGGGCCTTGATGTTACTGTCACGGCTGCCCAGTGGTAAGGAGCGGGAGTGGGCCGTGTTCATGCTCTTTACATATCATTCAATAATTCCGAGGCAACCATAGTTGTTCTCATCTTGGTCTGATGCCGCTAGGCTCATAATAAACTAAACACAACCCGCCCAACGGCATTCTAACGGGTCCCGTGCGGGAATGCGCTCGTGAGTGTCAGGTAGGGGTCAGCCCTCGCCCTGACTGACATCGTGCACAGGCGAACTCCTCAATTAAGGTTCCAGCGCGACAACTCGTCTATTGTACTTCATAGGAACTATGAAAAGTCTTATAGGGGGGTACGTGGATAT"""
    sites = locating_restriction_sites(dna_sequence)
    for site in sites:
        print(site[0], site[1])
