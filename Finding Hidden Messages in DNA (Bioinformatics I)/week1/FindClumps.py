from MostFreqKMers import find_most_freq_kmers

def find_clumps(genome, k, L, t):
    freq_table, _ = find_most_freq_kmers(genome[:L], k)
    clumps = set([kmer for kmer in freq_table.keys() if freq_table[kmer] >= t])

    for i in range(1, len(genome) - L + 1):
        toRemove = genome[i-1 : i-1+k]
        freq_table[toRemove] -= 1
        toAdd = genome[i+L-k: i+L]
        freq_table[toAdd] = freq_table.get(toAdd, 0) + 1
        if freq_table[toAdd] >= t:
            clumps.add(toAdd)
    return sorted(list(clumps))

if __name__ == '__main__':
    with open("dataset_4_5.txt") as file:
        lines = file.readlines()
        genome = lines[0].strip()
        k, L, t = map(int, lines[1].strip().split())
        print(*find_clumps(genome, k, L, t))
