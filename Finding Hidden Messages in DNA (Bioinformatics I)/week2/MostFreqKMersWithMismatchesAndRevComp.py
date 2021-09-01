from GetNeighbors import get_neighbors

import sys
import os
sys.path.append(os.path.abspath('../week1'))
from ReverseComplement import reverse_complement_dna

def most_frequent_kmers_with_mismatches_and_reverse_complements(genome, k, d):
    freq_table = {}
    for i in range(len(genome) - k + 1):
        kmer = genome[i : i+k]
        neighbors = set()
        get_neighbors(kmer, 0, d, neighbors)
        for neighbor in neighbors:
            freq_table[neighbor] = freq_table.get(neighbor, 0) + 1
            rev_comp = reverse_complement_dna(neighbor)
            freq_table[rev_comp] = freq_table.get(rev_comp, 0) + 1
            
    max_freq = max(freq_table[kmer] + freq_table[reverse_complement_dna(kmer)] for kmer in freq_table.keys())
    # print(max_freq)
    return [kmer for kmer in freq_table.keys() if freq_table[kmer] + freq_table[reverse_complement_dna(kmer)] == max_freq]


if __name__ == '__main__':
    with open("dataset_9_10.txt") as f:
        lines = f.readlines()
        genome = lines[0].strip()
        k, d = map(int, lines[1].strip().split())
        print(*most_frequent_kmers_with_mismatches_and_reverse_complements(genome, k, d))
