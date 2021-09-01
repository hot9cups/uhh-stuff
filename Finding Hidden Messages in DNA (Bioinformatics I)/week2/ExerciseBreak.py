from AppxPatMatch import approximate_pattern_matching

matches = approximate_pattern_matching('AAAAA', 'AACAAGCTGATAAACATTTAAAGAG', 2)
print(len(matches))
