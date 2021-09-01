def get_kmer_probability(profile, kmer):
    prob = 1
    for index, nucleotide in enumerate(kmer):
        prob *= profile[nucleotide][index]
    return prob


if __name__ == "__main__":
    profile = {
        "A": [0.2, 0.2, 0, 0, 0, 0, 0.9, 0.1, 0.1, 0.1, 0.3, 0],
        "C": [0.1, 0.6, 0, 0, 0, 0, 0, 0.4, 0.1, 0.2, 0.4, 0.6],
        "G": [0, 0, 1, 1, 0.9, 0.9, 0.1, 0, 0, 0, 0, 0],
        "T": [0.7, 0.2, 0, 0, 0.1, 0.1, 0, 0.5, 0.8, 0.7, 0.3, 0.4],
    }

    pattern = "ACGGGGATTACC"
    expected = 0.000839808
    print(round(get_kmer_probability(profile, pattern), 9) == expected)

    pattern = "TCGGGGATTTCC"
    expected = 0.0205753
    print(round(get_kmer_probability(profile, pattern), 7) == expected)

    pattern = "TCGTGGATTTCC"
    expected = 0
    print(get_kmer_probability(profile, pattern) == expected)
