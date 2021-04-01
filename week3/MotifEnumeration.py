import sys
import os
sys.path.append(os.path.abspath('../week2'))
from GetNeighbors import get_neighbors
from HammingDist import hamming_distance

def motif_enumeration(dna, k, d):
    Patterns = set()
    neighbors = set()
    for i in range(len(dna[0]) - k + 1):
        get_neighbors(dna[0][i:i+k], 0, d, neighbors)
    
    for i in range(1, len(dna)):
        dna_seq = dna[i]
        new_neighbors = set()
        for neighbor in neighbors:
            for j in range(len(dna_seq) - k + 1):
                if hamming_distance(neighbor, dna_seq[j:j+k], d) <= d:
                    break
            else:
                continue
            new_neighbors.add(neighbor)
        neighbors = new_neighbors
    return list(neighbors)


if __name__ == '__main__':
    with open("dataset_156_8.txt") as f:
        data = f.readlines()
        k, d = map(int, data[0].strip().split())
        dna = [item.strip() for item in data[1:]]
        kdMotifs = motif_enumeration(dna, k, d)
        #print(*kdMotifs)
        with open("out.txt", 'w') as output:
            output.write(" ".join(kdMotifs))  