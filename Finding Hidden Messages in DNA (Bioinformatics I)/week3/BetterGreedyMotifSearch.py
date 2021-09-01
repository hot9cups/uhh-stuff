from ProfileMostProbableKmer import profile_most_probable_kmer
from Counts import get_counts
from Profile import get_profile
from Score import get_score
# from Consensus import get_consensus

def better_greedy_motif_search(dna, k, t):
    best_motifs = [seq[:k] for seq in dna]
    least_score = get_score(dna = best_motifs)
    for idx in range(len(dna[0]) - k + 1):
        motifs = [dna[0][idx : idx + k]]
        for seq_idx in range(1, t):
            profile = get_profile(dna = motifs, laplacian_pseudocount = 1)
            next_motif = profile_most_probable_kmer(dna[seq_idx], k, profile)
            motifs.append(next_motif)
        curr_score = get_score(dna = motifs)
        if curr_score < least_score:
            least_score = curr_score
            best_motifs = motifs
    return best_motifs



if __name__ == '__main__':
    with open("dataset_160_9.txt") as f:
        k, t = map(int, f.readline().strip().split())
        dna = []
        for _ in range(t):
            dna.append(f.readline().strip())
        
        best_motifs = better_greedy_motif_search(dna, k, t)
        with open("output2.txt", "w") as output:
            for motif in best_motifs:
                output.write(motif+'\n')
        # print(get_consensus(dna = best_motifs))