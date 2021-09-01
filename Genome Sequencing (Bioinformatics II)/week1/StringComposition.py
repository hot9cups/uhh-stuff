def string_composition(text, k):
    composition = []
    for i in range(len(text) - k + 1):
        composition.append(text[i : i + k])
    return composition


if __name__ == "__main__":
    with open("dataset_197_3.txt") as file:
        lines = file.readlines()
        k = int(lines[0].strip())
        text = lines[1].strip()
        composition = string_composition(text, k)
        with open("outputStringComp.txt", "w") as f:
            f.write("\n".join(composition))
