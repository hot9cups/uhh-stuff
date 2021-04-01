def find_most_freq_kmers(text, k):
    freq_table = {}
    for i in range(len(text) - k + 1):
        pattern = text[i:i+k]
        freq_table[pattern] = freq_table.get(pattern, 0) + 1
    maxOccurrence = max(freq_table.values())
    ans = []
    for pattern, count in freq_table.items():
        if count == maxOccurrence:
            ans.append(pattern)
    return freq_table, sorted(ans)

if __name__ == '__main__':
    with open("dataset_2_13.txt") as file:
        lines = file.readlines()    
        text = lines[0].strip()
        k = int(lines[1].strip())
        
        freq_table, most_freq_kmers = find_most_freq_kmers(text, k)
        print(*most_freq_kmers)
