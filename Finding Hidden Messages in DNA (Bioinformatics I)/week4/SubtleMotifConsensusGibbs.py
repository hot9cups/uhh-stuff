from GibbsSampling import gibbs_sampler
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
        best_score, best_motifs = k * t, []
        start = time()
        for starts in range(20):
            score, motifs = gibbs_sampler(dna, k, t, 2000)
            if score < best_score:
                best_score = score
                best_motifs = motifs
        print(time() - start)
        print(get_consensus(dna=best_motifs))
        print(best_score)
