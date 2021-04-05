from Counts import get_counts
from copy import deepcopy

def get_consensus(counts = None, dna = None):
    if counts is None:
        counts = get_counts(dna)
    nucleotides = list("ACGT")
    
    col_count = 0
    for nucleotide in nucleotides:
        col_count += counts[nucleotide][0]
    
    consensus = []

    for index in range(len(counts["A"])):
        highest = -1
        most_common_nuc = ""
        for nucleotide in nucleotides:
            if counts[nucleotide][index] > highest:
                highest = counts[nucleotide][index]
                most_common_nuc = nucleotide
        consensus.append(most_common_nuc)
    return "".join(consensus)



if __name__ == '__main__':
    counts = {
        'A': [2, 2, 0, 0, 0, 0, 9, 1, 1, 1, 3, 0], 
        'C': [1, 6, 0, 0, 0, 0, 0, 4, 1, 2, 4, 6], 
        'G': [0, 0, 10, 10, 9, 9, 1, 0, 0, 0, 0, 0], 
        'T': [7, 2, 0, 0, 1, 1, 0, 5, 8, 7, 3, 4]
        }
    print(get_consensus(counts = counts))