from Counts import get_counts
from copy import deepcopy

def get_profile(counts = None, dna = None):
    if counts is None:
        counts = get_counts(dna)
    nucleotides = list("ACGT")
    profile = deepcopy(counts)

    col_count = 0
    for nucleotide in nucleotides:
        col_count += counts[nucleotide][0]
    
    for nucleotide in nucleotides:
        for index in range(len(profile[nucleotide])):
            profile[nucleotide][index] /= max(col_count, 1)
    
    return profile


if __name__ == '__main__':
    counts = {
        'A': [2, 2, 0, 0, 0, 0, 9, 1, 1, 1, 3, 0], 
        'C': [1, 6, 0, 0, 0, 0, 0, 4, 1, 2, 4, 6], 
        'G': [0, 0, 10, 10, 9, 9, 1, 0, 0, 0, 0, 0], 
        'T': [7, 2, 0, 0, 1, 1, 0, 5, 8, 7, 3, 4]
        }
    print(get_profile(counts = counts))