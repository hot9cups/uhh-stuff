def get_neighbors(formed, cur_idx, remaining, neighbors):
    if remaining == 0:
        neighbors.add(formed)
        return
    
    neighbors.add(formed)
    for i in range(cur_idx, len(formed) - remaining + 1):
        for nucleotide in "ATCG":
            get_neighbors(formed[:i] + nucleotide + formed[i+1:], i + 1, remaining - 1, neighbors)

if __name__ == '__main__':
    with open("dataset_3014_4.txt") as file:
        lines = file.readlines()    
        pattern = lines[0].strip()
        d = int(lines[1].strip())
        with open("out.txt", 'w') as output:
            neighbors = set()
            get_neighbors(pattern, 0, d, neighbors)
            output.write("\n".join(list(neighbors)))    



# official method, but slower
'''
from HammingDist import hamming_distance

def get_neighbors(formed, d):
    if d == 0:
        return {formed}
    if len(formed) == 1:
        return {'A', 'T', 'C', 'G'}
    neighborhood = set()
    suffix = formed[1:]
    suffix_neighbors = get_neighbors(suffix, d)
    for neighbor in suffix_neighbors:
        if hamming_distance(neighbor, suffix, d) < d:
            for nucleotide in "ATCG":
                neighborhood.add(nucleotide + neighbor)
        else:
            neighborhood.add(formed[0] + neighbor)
    return neighborhood

if __name__ == '__main__':
    with open("dataset_3014_4.txt") as file:
        lines = file.readlines()    
        pattern = lines[0].strip()
        d = int(lines[1].strip())
        with open("out.txt", 'w') as output:
            neighbors = get_neighbors(pattern, d, )
            output.write("\n".join(list(neighbors)))
'''

# Also if we need exactly d distance away neighbors
'''
def get_neighbors(formed, d):
    if d == 0:
        return {formed}
    if len(formed) == 1:
        return {'A', 'T', 'C', 'G'}
    neighborhood = set()
    suffix = formed[1:]
    suffix_neighbors = get_neighbors(suffix, d)
    for neighbor in suffix_neighbors:
        distance = hamming_distance(neighbor, suffix, d)
        if distance == d-1:
            for nucleotide in "ATCG":
                if nucleotide != formed[0]:
                    neighborhood.add(nucleotide + neighbor)
        elif distance == d:
            neighborhood.add(formed[0] + neighbor)
    return neighborhood
'''