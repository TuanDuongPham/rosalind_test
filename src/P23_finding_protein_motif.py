import requests
import asyncio
from helper.extract_fasta_seqences import extract_fasta_sequences

"""
N-glycosylation motif: N{P}[ST]{P} => N, not P, S or T, not P
"""


async def fetch_fasta(uniprot_id):
    url = f"http://www.uniprot.org/uniprot/{uniprot_id}.fasta"
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return False


def raw_id_to_list(protein_ids_raw):
    if "_" not in protein_ids_raw:
        return protein_ids_raw.strip().split()
    else:
        id_lines = protein_ids_raw.strip().splitlines()
        id_list = []
        for line in id_lines:
            id_list.append(line.split("_")[0])
        return id_list


async def find_motif_positions(protein_id):
    protein_id_list = raw_id_to_list(protein_id)
    protein_sequences = {}
    for id in protein_id_list:
        protein_seq = await fetch_fasta(id)
        if protein_seq:
            protein_sequences[id] = list(extract_fasta_sequences(protein_seq).values())[0]

    motif_positions = {}
    for id, sequence in protein_sequences.items():
        positions = []
        for i in range(len(sequence) - 3):
            if (sequence[i] == "N" and sequence[i + 1] != "P" and sequence[i + 2] in ["S", "T"] and sequence[i + 3] != "P"):
                positions.append(i + 1)
        if positions:
            motif_positions[id] = positions

    return motif_positions

if __name__ == "__main__":
    raw_id = """P04278_SSBP_HUMAN
P05783_K1CR_HUMAN
B4R8K2
A1X8C2
P04921_GLPC_HUMAN
A4J5V5
Q60960
P01047_KNL2_BOVIN
P81824_PABJ_BOTJA
P05231_IL6_HUMAN
Q2GBA3
Q0SU18
A4SQX2
P07725_CD8A_RAT
"""
    protein_seqs = asyncio.run(find_motif_positions(raw_id))
    for protein_id, positions in protein_seqs.items():
        print(protein_id)
        print(" ".join(map(str, positions)))

# Note for later refactor: Map the protein_id in the result again with the given id (input id) to print out full id as request
