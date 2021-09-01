def skew(genome):
    C_count, G_count = 0, 0
    skew_list = [0]
    for nucleotide in genome:
        if nucleotide == 'C':
            C_count += 1
        elif nucleotide == 'G':
            G_count += 1
        skew_list.append(G_count - C_count)
    return skew_list

if __name__ == '__main__':
    # genome = input()
    genome = 'TAAAGACTGCCGAGAGGCCAACACGAGTGCTAGAACGAGGGGCGTAAACGCGGGTCCGAT'
    print(*skew(genome))

