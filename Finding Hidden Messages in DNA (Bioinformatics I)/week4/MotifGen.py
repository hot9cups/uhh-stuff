import sys
import os

sys.path.append(os.path.abspath("../week3"))
from ProfileMostProbableKmer import profile_most_probable_kmer


def get_motifs(profile, dna):
    k = len(profile["A"])
    motifs = []
    for dna_seq in dna:
        motifs.append(profile_most_probable_kmer(dna_seq, k, profile))
    return motifs


if __name__ == "__main__":
    profile = {
        "A": [4 / 5, 0, 0, 1 / 5],
        "C": [0, 3 / 5, 1 / 5, 0],
        "G": [1 / 5, 1 / 5, 4 / 5, 0],
        "T": [0, 1 / 5, 0, 4 / 5],
    }
    dna = ["TTACCTTAAC", "GATGTCTGTC", "ACGGCGTTAG", "CCCTAACGAG", "CGTCAGAGGT"]
    expected = ["ACCT", "ATGT", "GCGT", "ACGA", "AGGT"]

    motifs = get_motifs(profile, dna)
    print(expected == motifs)
