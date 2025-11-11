def is_substring_in_all(substr, seqs):
    for s in seqs:
        if substr not in s:
            return False
    return True
