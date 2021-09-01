from MinSkew import min_skew
from MostFreqKMersWithMismatchesAndRevComp import most_frequent_kmers_with_mismatches_and_reverse_complements

if __name__ == '__main__':

    with open("Salmonella_enterica.txt") as f:
        genome = "".join(line.strip() for line in f.readlines()[1:])
        
        position = min_skew(genome)[0] # [3764856, 3764858], let's just work with the 1st one.
        window_ending_at_position = genome[position - 500 : position + 1]
        window_centred_at_position = genome[position - 500 : position + 500]
        window_starting_at_position = genome[position : position + 500]
        print(most_frequent_kmers_with_mismatches_and_reverse_complements(window_ending_at_position, 9, 1))
        print(most_frequent_kmers_with_mismatches_and_reverse_complements(window_centred_at_position, 9, 1))
        print(most_frequent_kmers_with_mismatches_and_reverse_complements(window_starting_at_position, 9, 1))