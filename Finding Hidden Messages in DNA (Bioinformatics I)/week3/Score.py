from Counts import get_counts
from copy import deepcopy

def get_score(counts = None, dna = None):
    if counts is None:
        counts = get_counts(dna)
    nucleotides = list("ACGT")
    
    col_count = 0
    for nucleotide in nucleotides:
        col_count += counts[nucleotide][0]
    
    score = 0

    for index in range(len(counts["A"])):
        highest = -1
        for nucleotide in nucleotides:
            highest = max(highest, counts[nucleotide][index])
        score += col_count - highest
    return score



if __name__ == '__main__':
    counts = {
        'A': [2, 2, 0, 0, 0, 0, 9, 1, 1, 1, 3, 0], 
        'C': [1, 6, 0, 0, 0, 0, 0, 4, 1, 2, 4, 6], 
        'G': [0, 0, 10, 10, 9, 9, 1, 0, 0, 0, 0, 0], 
        'T': [7, 2, 0, 0, 1, 1, 0, 5, 8, 7, 3, 4]
        }
    print(get_score(counts = counts))