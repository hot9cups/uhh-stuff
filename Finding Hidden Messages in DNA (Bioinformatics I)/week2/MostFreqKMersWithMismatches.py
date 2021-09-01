from GetNeighbors import get_neighbors
from AppxPatCount import approximate_pattern_count

def most_frequent_kmers_with_mismatches(genome, k, d):
    freq_table = {}
    for i in range(len(genome) - k + 1):
        kmer = genome[i : i+k]
        neighbors = set()
        get_neighbors(kmer, 0, d, neighbors)
        for neighbor in neighbors:
            freq_table[neighbor] = freq_table.get(neighbor, 0) + 1
    
    max_freq = max(freq_table[kmer] for kmer in freq_table.keys())
    return [kmer for kmer in freq_table.keys() if freq_table[kmer] == max_freq]

if __name__ == '__main__':
    with open("dataset_9_9.txt") as f:
        lines = f.readlines()
        genome = lines[0].strip()
        k, d = map(int, lines[1].strip().split())
        print(*most_frequent_kmers_with_mismatches(genome, k, d))



'''
def most_frequent_kmers_with_mismatches(genome, k, d):
    freq_table = {}
    for i in range(len(genome) - k + 1):
        kmer = genome[i : i+k]
        neighbors = get_neighbors(kmer, d)
        for neighbor in neighbors:
            freq_table[neighbor] = freq_table.get(neighbor, 0) + 1
    
    max_freq = max(freq_table[kmer] for kmer in freq_table.keys())
    return [kmer for kmer in freq_table.keys() if freq_table[kmer] == max_freq]
'''