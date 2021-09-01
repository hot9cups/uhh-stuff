def pattern_count(text, pattern):
    occurrences = 0 
    for i in range(len(text) - len(pattern) + 1):
        if(text[i: i+len(pattern)] == pattern):
            occurrences += 1
    return occurrences

if __name__ == '__main__':
    with open("dataset_2_6.txt") as file:
        lines = file.readlines()    
        text = lines[0].strip()
        pattern = lines[1].strip()

        print(pattern_count(text, pattern))
