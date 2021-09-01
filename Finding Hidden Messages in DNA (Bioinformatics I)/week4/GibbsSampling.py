from RandomMotifPicker import get_random_motifs
from RandomNumberGenerator import get_random_number
from KmerProbability import get_kmer_probability

import sys
import os
import random
from copy import deepcopy

sys.path.append(os.path.abspath("../week3"))
from Profile import get_profile
from Score import get_score


def gibbs_sampler(dna, k, t, runs=1):
    motifs = get_random_motifs(dna, k)
    best_motifs = deepcopy(motifs)
    best_score = get_score(dna=best_motifs)

    for times in range(runs):
        idx = random.randrange(0, t)
        motifs_without_motif_idx = [kmer for i, kmer in enumerate(motifs) if i != idx]
        profile = get_profile(dna=motifs_without_motif_idx, laplacian_pseudocount=1)
        probabilities = [
            get_kmer_probability(profile, dna[idx][i : i + k])
            for i in range(len(dna[idx]) - k + 1)
        ]
        random_weighted_kmer_idx = get_random_number(probabilities)
        motif_idx = dna[idx][random_weighted_kmer_idx : random_weighted_kmer_idx + k]
        motifs[idx] = motif_idx
        motifs_score = get_score(dna=motifs)
        if motifs_score < best_score:
            best_score = motifs_score
            best_motifs = deepcopy(motifs)

    return best_score, best_motifs


if __name__ == "__main__":
    with open("dataset_163_4.txt") as f:
        k, t, N = map(int, f.readline().strip().split())
        dna = [f.readline().strip() for _ in range(t)]

    best_score, best_motifs = k * t, []
    for starts in range(20):
        score, motifs = gibbs_sampler(dna, k, t, N)
        if score < best_score:
            best_score = score
            best_motifs = motifs

    with open("gibbs_sampler_output.txt", "w") as output:
        output.write("\n".join(best_motifs))

    print(best_score)
