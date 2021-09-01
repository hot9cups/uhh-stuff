from BetterGreedyMotifSearch import better_greedy_motif_search
from Consensus import get_consensus

import os.path

def generate_clean_data(filename):
    with open(filename) as input_file:
        with open("cleaned_" + filename, 'w') as output_file:
            for line in input_file.readlines():
                line = line.replace("*","")
                output_file.write(line)


if __name__ == '__main__':
    if not os.path.isfile("cleaned_subtle_motif_dataset.txt"):
        generate_clean_data("subtle_motif_dataset.txt")

    with open("cleaned_subtle_motif_dataset.txt") as f:
        k = 15
        dna = [line.strip() for line in f.readlines()]
        t = len(dna)
        
        best_motifs = better_greedy_motif_search(dna, k, t)
        print(get_consensus(dna = best_motifs))