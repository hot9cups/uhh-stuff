def get_debruijn_from_kmers(kmers):
    deBruijn = dict()
    for kmer in kmers:
        deBruijn.setdefault(kmer[:-1], []).append(kmer[1:])
    return deBruijn

if __name__ == "__main__":
    with open("dataset_200_8.txt") as file:
        kmers = [line.strip() for line in file.readlines()]
        deBruijn = get_debruijn_from_kmers(kmers)
        with open("outputDebruijnGraphFromKmers.txt", "w") as f:
            f.write("\n".join((k + ' -> ' + ",".join(sorted(v)) for k, v in sorted(deBruijn.items()))))