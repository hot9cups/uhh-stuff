from collections import Counter

def get_counts(motifs):
    counts = dict()
    nucleotides = list("ACGT")
    for nucleotide in nucleotides:
        counts[nucleotide] = list()    
    for i in range(len(motifs[0])):
        col_i = [row[i] for row in motifs]
        freq = Counter(col_i)
        for nucleotide in nucleotides:
            counts[nucleotide].append(freq.get(nucleotide, 0))
    return counts


if __name__ == '__main__':
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
                "TCGGGTATAACC"
            ]
    print(get_counts(Motifs))
    