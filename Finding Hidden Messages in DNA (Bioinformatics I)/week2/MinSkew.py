def min_skew(genome):
    C_count, G_count = 0, 0
    min_diff = len(genome)
    positions = []
    for index, nucleotide in enumerate(genome, 1):
        if nucleotide == 'C':
            C_count += 1
        elif nucleotide == 'G':
            G_count += 1
            
        diff = G_count - C_count 
        
        if diff < min_diff:
            min_diff = diff
            positions = [index]
        elif diff == min_diff:
            positions.append(index)
            
    return positions

if __name__ == '__main__':
    with open("dataset_7_10.txt") as f:
        genome = f.read().split()[0]
        print(*min_skew(genome))


'''
def min_skew(genome):
    C_count, G_count = 0, 0
    min_diff = len(genome)
    positions = {}
    for index, nucleotide in enumerate(genome, 1):
        if nucleotide == 'C':
            C_count += 1
        elif nucleotide == 'G':
            G_count += 1
            
        diff = G_count - C_count 
        
        if diff < min_diff:
            positions.clear()                    # positions.pop(min_diff, "None")
            min_diff = diff
            positions[diff] = [index]
        elif diff == min_diff:
            positions[diff].append(index)
            
    return positions[min_diff]

if __name__ == '__main__':
    genome = input()
    print(*min_skew(genome))
'''