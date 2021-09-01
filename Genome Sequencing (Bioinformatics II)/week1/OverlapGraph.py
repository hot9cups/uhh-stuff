def getOverlapGraph(kmers):
    prefix = {}
    for kmer in kmers:
        prefix.setdefault(kmer[:-1], []).append(kmer)
    overlapGraph = {}

    for kmer in kmers:
        suffix = kmer[1:]
        if suffix in prefix:
            overlapGraph.setdefault(kmer, []).extend(prefix.get(suffix))
    return overlapGraph


if __name__ == "__main__":
    with open("dataset_198_10.txt") as file:
        kmers = [line.strip() for line in file.readlines()]
        overlapGraph = getOverlapGraph(kmers)
        with open("outputOverlapGraph.txt", "w") as f:
            temp = []
            for k, v in overlapGraph.items():
                temp.append(k + " -> " + ",".join(v))
            f.write("\n".join(temp))
