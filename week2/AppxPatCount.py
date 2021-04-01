from HammingDist import hamming_distance

def approximate_pattern_count(pattern, genome, d):
    matches = 0
    for i in range(len(genome) - len(pattern) + 1):
        if hamming_distance(genome[i: i+len(pattern)], pattern, d) <= d:
            matches += 1
    return matches

if __name__ == '__main__':
    with open("dataset_9_6.txt") as file:
        lines = file.readlines()    
        pattern = lines[0].strip()
        genome = lines[1].strip()
        d = int(lines[2].strip())
        print(approximate_pattern_count(pattern, genome, d))



'''
from AppxPatMatch import approximate_pattern_matching

if __name__ == '__main__':
    with open("dataset_9_6.txt") as file:
        lines = file.readlines()    
        pattern = lines[0].strip()
        genome = lines[1].strip()
        d = int(lines[2].strip())
        print(len(approximate_pattern_matching(pattern, genome, d)))
'''
