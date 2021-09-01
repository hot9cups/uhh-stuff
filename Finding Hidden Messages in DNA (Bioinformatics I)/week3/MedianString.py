"""import sys
import os
from itertools import product
sys.path.append(os.path.abspath('../week2'))
# from GetNeighbors import get_neighbors
from HammingDist import hamming_distance
from time import time

def median_string(dna, k):
    neighbors = set()
    # get_neighbors("A"*k, 0, k, neighbors)
    best_score = k * len(dna)
    best_motif = ""
    for pattern in product(('A', 'T', 'C', 'G'), repeat = k):
        pattern = "".join(pattern)
        score = 0
        for dna_seq in dna:
            least_dist = k
            for i in range(len(dna_seq) - k + 1):
                dist = hamming_distance(pattern, dna_seq[i:i+k])
                if dist < least_dist:
                    least_dist = dist
            score += least_dist
        if score <= best_score:
            best_score = score
            best_motif = pattern
    return best_motif


if __name__ == '__main__':
    with open("dataset_158_9.txt") as f:
        start = time()
        data = f.readlines()
        k = int(data[0].strip())
        dna = []
        for i in range(1, len(data)):
            dna.append(data[i].strip())

    print(median_string(dna, k))
    print(time() - start)
"""    

import sys
import os
sys.path.append(os.path.abspath('../week2'))
from GetNeighbors import get_neighbors
from HammingDist import hamming_distance
from time import time

def median_string(dna, k):
    neighbors = set()
    get_neighbors("A"*k, 0, k, neighbors)
    best_score = k * len(dna)
    best_motif = ""
    for pattern in neighbors:
        score = 0
        for dna_seq in dna:
            least_dist = k
            for i in range(len(dna_seq) - k + 1):
                dist = hamming_distance(pattern, dna_seq[i:i+k])
                if dist < least_dist:
                    least_dist = dist
            score += least_dist
        if score <= best_score:
            best_score = score
            best_motif = pattern
    return best_motif


if __name__ == '__main__':
    with open("dataset_158_9.txt") as f:
        start = time()
        data = f.readlines()
        k = int(data[0].strip())
        dna = []
        for i in range(1, len(data)):
            dna.append(data[i].strip())

    print(median_string(dna, k))
    print(time() - start)
    