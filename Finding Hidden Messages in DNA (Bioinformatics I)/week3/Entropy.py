from Profile import get_profile
import math


def get_entropy(profile=None, dna=None, laplacian_pseudocount=0):
    if profile is None:
        profile = get_profile(dna=dna, laplacian_pseudocount=laplacian_pseudocount)

    nucleotides = list("ACGT")
    total_entropy = 0

    for col in range(len(profile["A"])):
        column_entropy = 0
        for nucleotide in nucleotides:
            prob = profile[nucleotide][col]
            if prob > 0:
                column_entropy += -1 * prob * math.log2(prob)
        total_entropy += column_entropy

    return total_entropy


if __name__ == "__main__":
    Motifs = [
        "TCGGGGGTTTTT",
        "CCGGTGACTTAC",
        "ACGGGGATTTTC",
        "TTGGGGACTTTT",
        "AAGGGGACTTCC",
        "TTGGGGACTTCC",
        "TCGGGGATTCAT",
        "TCGGGGATTCCT",
        "TAGGGGAACTAC",
        "TCGGGTATAACC",
    ]
    print(get_entropy(dna=Motifs))
