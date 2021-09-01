def pattern_matching(pattern, genome):
    positions = []
    for i in range(len(genome) - len(pattern) + 1):
        if(genome[i: i+len(pattern)] == pattern):
            positions.append(i)
    return positions

if __name__ == '__main__':
    with open("dataset_3_5.txt") as file:
        lines = file.readlines()    
        pattern = lines[0].strip()
        genome = lines[1].strip()
        print(*pattern_matching(pattern, genome))