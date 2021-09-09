def get_debruijn_graph(text, k):    
    k -= 1
    deBruijn = dict()

    for i in range(len(text) - k + 1 - 1):
        curNode = text[i: i+k]
        nextNode = text[i+1: i+1+k]
        deBruijn.setdefault(curNode, []).append(nextNode)
    return deBruijn


if __name__ == "__main__":
    with open("dataset_199_6.txt") as file:
        lines = file.readlines()
        k = int(lines[0].strip())
        text = lines[1].strip()
        deBruijn = get_debruijn_graph(text, k)
        with open("outputDebruijnGraph.txt", "w") as f:
            f.write("\n".join((k + ' -> ' + ",".join(sorted(v)) for k, v in sorted(deBruijn.items()))))
