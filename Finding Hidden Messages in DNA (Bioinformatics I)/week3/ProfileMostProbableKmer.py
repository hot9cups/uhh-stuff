def profile_most_probable_kmer(text, k, profile):
    highest_prob = -1
    most_probable_kmer = ""
    for i in range(len(text) - k + 1):
        kmer = text[i : i+k]
        prob = 1
        for index, nucleotide in enumerate(kmer):
            prob *= profile[nucleotide][index]
        if prob > highest_prob:
            highest_prob = prob
            most_probable_kmer = kmer
    return most_probable_kmer

    

if __name__ == '__main__':
    with open("dataset_159_3.txt") as f:
        text = f.readline().strip()
        k = int(f.readline().strip())
        profile = {}
        for letter in ['A', 'C', 'G', 'T']:
            profile[letter] = [float(item) for item in f.readline().strip().split()]
        print(profile_most_probable_kmer(text, k, profile))

