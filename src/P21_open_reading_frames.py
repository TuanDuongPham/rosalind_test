from helper.extract_fasta_seqences import extract_fasta_sequences
from helper.rna_codon_dict import RNA_CONDON_DICT as rna_codon_dict
from P02_transcribing_DNA_to_RNA import transcribing_dna_to_rna


def find_open_reading_frames(dna_sequence):
    rna_sequence = transcribing_dna_to_rna(dna_sequence)
    start_positions = []
    stop_positions = []

    for i in range(len(rna_sequence) - 2):
        codon = rna_sequence[i:i+3]
        if codon == 'AUG':
            start_positions.append(i)
        elif codon in ['UAA', 'UAG', 'UGA']:
            stop_positions.append(i)

    posible_orfs = []
    sorted_start_positions = sorted(start_positions)
    sorted_stop_positions = sorted(stop_positions)
    for i in sorted_start_positions:
        for j in sorted_stop_positions:
            if j > i and (j - i) % 3 == 0:
                posible_orfs.append(rna_sequence[i:(j + 3)])
                break

    candidate_proteins = []
    for orf in posible_orfs:
        protein = ''
        for k in range(0, len(orf), 3):
            codon = orf[k:k+3]
            amino_acid = rna_codon_dict.get(codon, '')
            if amino_acid == 'Stop':
                break
            protein += amino_acid

        candidate_proteins.append(protein)

    return candidate_proteins


def find_candidate_proteins_from_fasta(fasta_sequences):
    dna_sequences = list(extract_fasta_sequences(fasta_sequences).values())[0]

    reverse_sequence = dna_sequences[::-1].translate(str.maketrans({'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}))

    all_sequences = [dna_sequences, reverse_sequence]
    candidate_proteins = []
    for seq in all_sequences:
        proteins = find_open_reading_frames(seq)
        for protein in proteins:
            if protein not in candidate_proteins:
                candidate_proteins.append(protein)

    return candidate_proteins


if __name__ == "__main__":
    fasta_sequences = """>Rosalind_4378
GCACGCGTGGGAGTAGCAGTGAAGGTGGACTATGTCACAGACAGATGCCCCAGGACGCCT
TTATTGGCTCCGCGCGACCGTTTAGGGACTGTACAATGTGGTCAGCGGGAGACATCCGCG
GGGACCAGCACATGTAAGTGATTTTGTGTCGAGCAACTGTTAATGTGTATATAACAACGT
GACACTGGCCCCTTCCGGGAATGTAGACTCGCAAACCCAAGACGTGGTAGCATCGTAGAC
CACGAGTTGCCGTTGAGGGTCCTCTCATCGGGTAATAGCAAGCATATCATGTGTGGGGCG
CTCTCCGAAAGCGTCAGTCTAAGGTTCGAAATGTAGCATTGGCACTTAGGGCGCACGGCT
CGCGCAACTTAATCGCCTCTGTGTATCGACAGCAAAAGCCCAACGTTTTCATGCAGAATA
CAGACTTACCGCTGCCTCTGGTACTCATGACGGAGAGTTTACTCACGAAACAACCCAATT
AGCTAATTGGGTTGTTTCGTGAGTAAACTCTCCGTCATAACTTCTATCGAACAATACTTG
CATATGCACAGCAGCTTCTGATAAGTCATTCGCGGGGCCTTTTCCATACCTACAGGTTAC
ATGCGCGGAAATTGGACGGTACCGCCAATCGAAATACTGGGAAGCCTGTTCGCTACCCGA
CGACTTAAGCTTGGCCCCATCAAACTGAAAATTATTACCGTCCACACAGTCTGGCCTGAA
GACCCGTAGCCCTGGTTCGCCCTAAGGTAGCCTACTGCCCCTATCACACCGTCCTAACCA
CACTAGTCGTCACTTAAGTTTCCGACAATCTGCGCGGAAGAGCCTGGCCCTCTCTAGCAC
TGGTGAGACCATTTAATGGGGACTACCAGAAACGAGTCTCAACCCTGCGGACTCTCCGAA
GATCTGATAATGATTCCACTGCTACTACGATTGGTGTTGACAAAGAAATGCATAGACGCT
AGTA"""

    candidate_proteins = find_candidate_proteins_from_fasta(fasta_sequences)
    for protein in candidate_proteins:
        print(protein)
