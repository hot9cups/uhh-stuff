def spell_string(genomePath):
    genome = []
    genome.append(genomePath[0])
    for i in range(1, len(genomePath)):
        genome.append(genomePath[i][-1])
    return "".join(genome)


if __name__ == "__main__":
    with open("dataset_198_3.txt") as file:
        lines = file.readlines()
        genomePath = [line.strip() for line in lines]
        genome = spell_string(genomePath)
        with open("outputSpellString.txt", "w") as f:
            f.write(genome)
