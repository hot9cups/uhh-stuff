import random


def get_random_motifs(dna, k):
    motifs = []
    for dna_seq in dna:
        idx = random.randrange(0, len(dna_seq) - k + 1)
        motifs.append(dna_seq[idx : idx + k])
    return motifs
