def hamming_distance(word1, word2, limit = None):
    mismatches = 0
    for letter1, letter2 in zip(word1, word2):
        if letter1 != letter2:
            mismatches += 1
        if limit is not None and mismatches > limit:
            return mismatches
    return mismatches

if __name__ == '__main__':
    with open("dataset_9_3.txt") as f:
        data = f.readlines()
        word1 = data[0].strip()
        word2 = data[1].strip()
        print(hamming_distance(word1, word2))