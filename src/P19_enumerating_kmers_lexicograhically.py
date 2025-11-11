def enumerate_kmers(symbols, n):
    symbols_list = list(symbols.split(" "))
    if n == 1:
        return symbols_list

    kmer_list = []
    for symbol in symbols_list:
        smaller_kmers = enumerate_kmers(symbols, n - 1)
        for kmer in smaller_kmers:
            kmer_list.append(symbol + kmer)

    return sorted(kmer_list)


if __name__ == "__main__":
    symbols = "A B C D"
    n = 4
    kmers = enumerate_kmers(symbols, n)
    for kmer in kmers:
        print(kmer)
