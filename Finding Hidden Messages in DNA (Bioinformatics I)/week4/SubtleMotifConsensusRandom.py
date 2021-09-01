from RandomizedMotifSearch import randomized_motif_search
import sys
import os

sys.path.append(os.path.abspath("../week3"))
from Consensus import get_consensus

from time import time

if __name__ == "__main__":
    with open("../week3/cleaned_subtle_motif_dataset.txt") as f:
        k = 15
        dna = [line.strip() for line in f.readlines()]
        t = len(dna)
        start = time()
        best_motifs, best_score = randomized_motif_search(dna, k, t, 750)
        print(time() - start)
        print(get_consensus(dna=best_motifs))
        print(best_score)
