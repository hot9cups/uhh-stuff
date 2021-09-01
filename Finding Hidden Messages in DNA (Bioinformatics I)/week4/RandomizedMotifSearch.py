from MotifGen import get_motifs
from RandomMotifPicker import get_random_motifs

import sys
import os

sys.path.append(os.path.abspath("../week3"))
from Profile import get_profile
from Score import get_score


def randomized_motif_search(dna, k, t, runs=1):
    final_motifs = []
    final_motifs_score = k * t
    for times in range(runs):
        best_motifs = get_random_motifs(dna, k)
        best_score = get_score(dna=best_motifs)
        while True:
            profile = get_profile(dna=best_motifs, laplacian_pseudocount=1)
            next_motifs = get_motifs(profile, dna)
            next_motifs_score = get_score(dna=next_motifs)
            if next_motifs_score < best_score:
                best_score = next_motifs_score
                best_motifs = next_motifs
            else:
                break

        if best_score < final_motifs_score:
            final_motifs_score = best_score
            final_motifs = best_motifs

    return final_motifs, final_motifs_score


if __name__ == "__main__":
    with open("dataset_161_5.txt") as f:
        k, t = map(int, f.readline().strip().split())
        dna = [f.readline().strip() for _ in range(t)]
    best_motifs, best_score = randomized_motif_search(dna, k, t, 1000)
    with open("ex1output.txt", "w") as output:
        output.write("\n".join(best_motifs))
