from PatternMatching import pattern_matching

with open("Vibrio_cholerae.txt") as file:
    genome = file.read().strip()
    pattern = "CTTGATCAT"
    print(*pattern_matching(pattern, genome))
