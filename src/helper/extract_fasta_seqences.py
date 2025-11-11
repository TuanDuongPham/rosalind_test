def extract_fasta_sequences(fasta_file_contents):
    dna_sequence_dict = {}
    lines_list = fasta_file_contents.splitlines()
    for i in range(len(lines_list)):
        if lines_list[i].startswith('>'):
            sequence_id = lines_list[i][1:]
            dna_sequence_dict[sequence_id] = ""
        else:
            dna_sequence_dict[sequence_id] += lines_list[i]

    return dna_sequence_dict
