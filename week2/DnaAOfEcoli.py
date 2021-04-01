# just a personal exercise to find DnaA box of e-coli based on week2's learnings

from MinSkew import min_skew
from MostFreqKMersWithMismatchesAndRevComp import most_frequent_kmers_with_mismatches_and_reverse_complements

if __name__ == '__main__':

    with open("E_coli.txt") as f:
        genome = f.read().strip()
        position = min_skew(genome)[0] # [3923620, 3923621, 3923622, 3923623], let's just work with the 1st one.
        window_ending_at_position = genome[position - 500 : position + 1]
        window_centred_at_position = genome[position - 250 : position + 250]
        window_starting_at_position = genome[position : position + 500]
        print(most_frequent_kmers_with_mismatches_and_reverse_complements(window_ending_at_position, 9, 1))
        print(most_frequent_kmers_with_mismatches_and_reverse_complements(window_centred_at_position, 9, 1))
        print(most_frequent_kmers_with_mismatches_and_reverse_complements(window_starting_at_position, 9, 1))
        
'''
If we assign 1 score to pattern with 1 mismatch, and 2 scores to pattern with no mismatch, we can say that the higher the score, 
the less the mismatches are. If we further group the pairs of reverse complement, we can get a list the pairs, ordering by their total score:

6  TTATCCACA (3)  TGTGGATAA (3)
6  GTGGATAAC (3)  GTTATCCAC (3)
6  GCTGGGATC (3)  GATCCCAGC (3)
--------------------------------
5  TGATCCCAG (2)  CTGGGATCA (3)
5  CCAGGATCC (2)  GGATCCTGG (3)
5  AGCTGGGAT (3)  ATCCCAGCT (2)
4  TGATCAACA (3)  TGTTGATCA (1)
4  GATCTTCTG (2)  CAGAAGATC (2)
4  AGAACAACA (2)  TGTTGTTCT (2)
4  GTTGATCCT (3)  AGGATCAAC (1)
4  TGTGAATAA (2)  TTATTCACA (2)
4  AGGATCCTT (1)  AAGGATCCT (3)
4  GATCAACAG (2)  CTGTTGATC (2)
4  AGATCTCTT (3)  AAGAGATCT (1)
4  AATGATCCG (3)  CGGATCATT (1)
4  TGGATAACC (2)  GGTTATCCA (2)
4  TCTGGATAA (3)  TTATCCAGA (1)
Apparently, the first 6 pairs of kmer are those mentioned in the text above. It could be a coincidence, 
but I guess normally we would start experimenting on those with less mismatches first.
'''

'''
STOP and Think: Salmonella typhimurium is a close relative of E. coli that causes typhoid fever and foodborne illness. 
After having learned what DnaA boxes look like in E. coli, how would you look for DnaA boxes in Salmonella enterica?

1)Find approximate location of OriC using minskew
2)Use MostFreqKMersWithMismatchesAndRevComp to find most freq 9 mers(window starting, ending and centred at the approximate location of OriC)
3)Compare these with DnaA boxes of E-coli, using HammingDistance and get the closest.
'''
