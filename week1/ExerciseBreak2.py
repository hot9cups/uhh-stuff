from FindClumps import find_clumps

with open("E_coli.txt") as file:
    genome = file.read().strip()
    print(len(find_clumps(genome, 9, 500, 3)))
