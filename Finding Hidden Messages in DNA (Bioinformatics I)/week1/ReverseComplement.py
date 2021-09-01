def reverse_complement_dna(DNA):
    compliments = {"A" : "T", "T" : "A", "C" : "G", "G" : "C"}
    rev_comp = []
    for letter in DNA:
        rev_comp.append(compliments[letter])
    return "".join(rev_comp[::-1])

if __name__ == '__main__':
    with open("dataset_3_2.txt") as file:
        lines = file.readlines()    
        DNA = lines[0].strip()
        print(reverse_complement_dna(DNA))
