from GibbsSampling import gibbs_sampler
import sys
import os

sys.path.append(os.path.abspath("../week3"))
from Consensus import get_consensus
from Entropy import get_entropy

from time import time

if __name__ == "__main__":
    with open("DosR.txt") as f:
        dna = [line.strip() for line in f.readlines()]
        total_time = 0
        print(
            "Time taken".ljust(13),
            "K".ljust(6),
            "Consensus".ljust(26),
            "Score".ljust(9),
            "Entropy".ljust(10),
            "Score/K".ljust(10),
            "Entropy/K",
        )
        print()
        for k in range(9, 23):
            t = len(dna)
            best_score, best_motifs = k * t, []
            for repeat in range(7):
                start = time()
                for starts in range(20):
                    score, motifs = gibbs_sampler(dna, k, t, 2000)
                    if score < best_score:
                        best_score = score
                        best_motifs = motifs

                elapsed = time() - start
                total_time += elapsed
                entropy = get_entropy(dna=best_motifs)
                print(
                    f"{round(elapsed,4):<13}",
                    f"{k:<6}",
                    f"{get_consensus(dna=best_motifs):<26}",
                    f"{best_score:<9}",
                    f"{round(entropy, 4):<10}",
                    f"{round(best_score / k, 4):<10}",
                    f"{round(entropy / k, 4)}",
                )
            print()
        print(f"Total Time = {total_time}")

"""
Time taken    Consensus                  Score     K      Score/k

42.7521       ATCGGCCCT                  18        9      2.0
42.0927       GCCGCCGGG                  17        9      1.8889
44.0874       GCCGCCGGG                  17        9      1.8889

48.6445       CTATCGGCCC                 19        10     1.9
47.1165       CTATCGGCCC                 19        10     1.9
46.8864       CTATCGGCCC                 19        10     1.9

48.0696       GGACTTCCGGC                20        11     1.8182
49.0161       GGACTTCCGGC                20        11     1.8182
49.377        GGACTTCCGGC                20        11     1.8182

51.8811       GACTTCCGGCCC               24        12     2.0
54.5945       GGACTTCCGGCC               23        12     1.9167
59.6541       GGACTTCCGGCC               23        12     1.9167

59.4374       GGACCAACGACCC              28        13     2.1538
61.4914       GGACCAACGACCC              28        13     2.1538
59.0218       GGACCAACGACCC              28        13     2.1538

63.2716       GGGACCTACGTCCC             31        14     2.2143
65.0845       GGGACCTACGTCCC             31        14     2.2143
62.5478       GGGACCTACGTCCC             31        14     2.2143

67.444        GGACTTACGGCCCTA            35        15     2.3333
68.8122       GGACTTACGGCCCTA            35        15     2.3333
67.2896       GGACTTACGGCCCTA            35        15     2.3333

78.775        GGGACCTACGTCCCTA           38        16     2.375
66.9198       GGGACCTACGTCCCTA           38        16     2.375
71.0349       GGGACCTACGTCCCTA           38        16     2.375

70.3          GGGGACCTACGTCCCTA          43        17     2.5294
72.8276       GGGGACCTACGTCCCTA          43        17     2.5294
69.567        GGGGACCTACGTCCCTA          43        17     2.5294

74.7774       GGGACCTACGTCCCTAGC         46        18     2.5556
72.9651       GGGACCTACGTCCCTAGC         46        18     2.5556
80.1293       GGGACCTACGTCCCTAGC         46        18     2.5556

87.1764       GGGACCTACGTCCCTAGCC        50        19     2.6316
78.677        GGGACCTACGTCCCTAGCC        50        19     2.6316
70.6722       GGGACCTACGTCCCTAGCC        50        19     2.6316

88.5342       GGGGACCTACGTCCCTAGCC       55        20     2.75
80.984        GGGGACCTACGTCCCTAGCC       55        20     2.75
77.6738       GGGGACCTACGTCCCTAGCC       55        20     2.75

80.3123       TGGGGACCTACGTCCCTAGCC      60        21     2.8571
73.6894       TGGGGACCTACGTCCCTAGCC      60        21     2.8571
74.0807       TGGGGACCTACGTCCCTAGCC      60        21     2.8571

76.31         GGGGACCTACGTCCCCAGCCCC     65        22     2.9545
79.6426       GGGGACCTACGTCCCCAGCCCC     65        22     2.9545
77.5019       GGGGACCTACGTCCCCAGCCCC     65        22     2.9545

Total Time = 2761.1230578422546
"""

"""
Time taken    K      Consensus                  Score     Entropy    Score/K    Entropy/K

42.798        9      CCATCGGCC                  17        5.8315     1.8889     0.6479
41.791        9      CCATCGGCC                  17        5.8315     1.8889     0.6479
41.789        9      CCATCGGCC                  17        5.8315     1.8889     0.6479
41.938        9      GGCGGGGAC                  16        6.2115     1.7778     0.6902
41.93         9      GGCGGGGAC                  16        6.2115     1.7778     0.6902
43.1295       9      GGCGGGGAC                  16        6.2115     1.7778     0.6902
43.752        9      GGCGGGGAC                  16        6.2115     1.7778     0.6902

45.898        10     AACGACCCCA                 20        7.3721     2.0        0.7372
47.1255       10     AACGACCCCA                 20        7.3721     2.0        0.7372
48.323        10     GACTTCCGGC                 19        7.6205     1.9        0.7621
52.7435       10     GACTTCCGGC                 19        7.6205     1.9        0.7621
50.5749       10     GACTTCCGGC                 19        7.6205     1.9        0.7621
51.7226       10     GACTTCCGGC                 19        7.6205     1.9        0.7621
47.128        10     GACTTCCGGC                 19        7.6205     1.9        0.7621

48.6211       11     GACTTCCGGCC                22        8.3867     2.0        0.7624
49.526        11     GGACTTCCGGC                20        8.4327     1.8182     0.7666
51.767        11     GGACTTCCGGC                20        8.4327     1.8182     0.7666
50.001        11     GGACTTCCGGC                20        8.4327     1.8182     0.7666
48.235        11     GGACTTCCGGC                20        8.4327     1.8182     0.7666
47.839        11     GGACTTCCGGC                20        8.4327     1.8182     0.7666
47.956        11     GGACTTCCGGC                20        8.4327     1.8182     0.7666

50.5          12     GGACTTCCGGCC               23        9.6624     1.9167     0.8052
50.56         12     GGACTTCCGGCC               23        9.6624     1.9167     0.8052
50.5835       12     GGACTTCCGGCC               23        9.6624     1.9167     0.8052
50.751        12     GGACTTCCGGCC               23        9.6624     1.9167     0.8052
51.265        12     GGACTTCCGGCC               23        9.6624     1.9167     0.8052
50.917        12     GGACTTCCGGCC               23        9.6624     1.9167     0.8052
51.519        12     GGACTTCCGGCC               23        9.6624     1.9167     0.8052

57.962        13     GGACCAACGGCCC              28        9.5737     2.1538     0.7364
58.1106       13     GGACCAACGGCCC              28        9.5737     2.1538     0.7364
60.1243       13     GGACCAACGGCCC              28        9.5737     2.1538     0.7364
56.288        13     GGACCAACGGCCC              28        9.5737     2.1538     0.7364
58.258        13     GGACCAACGGCCC              28        9.5737     2.1538     0.7364
58.48         13     GGACCAACGGCCC              28        9.5737     2.1538     0.7364
58.958        13     GGACCAACGGCCC              28        9.5737     2.1538     0.7364

65.6972       14     GGGACCTACGTCCC             31        10.5811    2.2143     0.7558
63.5314       14     GGGACCTACGTCCC             31        10.5811    2.2143     0.7558
60.288        14     GGGACCTACGTCCC             31        10.5811    2.2143     0.7558
65.2396       14     GGGACCTACGTCCC             31        10.5811    2.2143     0.7558
70.4203       14     GGGACCTACGTCCC             31        10.5811    2.2143     0.7558
63.4186       14     GGGACCTACGTCCC             31        10.5811    2.2143     0.7558
62.106        14     GGGACCTACGTCCC             31        10.5811    2.2143     0.7558

66.3962       15     GGACTTACGGCCCTA            35        11.3718    2.3333     0.7581
62.067        15     GGACTTACGGCCCTA            35        11.3718    2.3333     0.7581
62.674        15     GGACTTACGGCCCTA            35        11.3718    2.3333     0.7581
61.5606       15     GGACTTACGGCCCTA            35        11.3718    2.3333     0.7581
61.624        15     GGACTTACGGCCCTA            35        11.3718    2.3333     0.7581
63.861        15     GGACTTACGGCCCTA            35        11.3718    2.3333     0.7581
64.655        15     GGACTTACGGCCCTA            35        11.3718    2.3333     0.7581

68.7975       16     GGGACCTACGTCCCTA           38        13.1953    2.375      0.8247
67.872        16     GGGACCTACGTCCCTA           38        13.1953    2.375      0.8247
66.692        16     GGGACCTACGTCCCTA           38        13.1953    2.375      0.8247
65.729        16     GGGACCTACGTCCCTA           38        13.1953    2.375      0.8247
67.1991       16     GGGACCTACGTCCCTA           38        13.1953    2.375      0.8247
67.336        16     GGGACCTACGTCCCTA           38        13.1953    2.375      0.8247
66.446        16     GGGACCTACGTCCCTA           38        13.1953    2.375      0.8247

72.039        17     GGGACCTACGTCCCTAG          43        14.0559    2.5294     0.8268
71.5955       17     GGGACCTACGTCCCTAG          43        14.0559    2.5294     0.8268
67.967        17     GGGACCTACGTCCCTAG          43        14.0559    2.5294     0.8268
69.072        17     GGGACCTACGTCCCTAG          43        14.0559    2.5294     0.8268
68.642        17     GGGACCTACGTCCCTAG          43        14.0559    2.5294     0.8268
70.957        17     GGGACCTACGTCCCTAG          43        14.0559    2.5294     0.8268
67.7445       17     GGGACCTACGTCCCTAG          43        14.0559    2.5294     0.8268

69.8693       18     GGGACCTACGTCCCTAGC         46        15.5511    2.5556     0.8639
67.215        18     GGGACCTACGTCCCTAGC         46        15.5511    2.5556     0.8639
68.4995       18     GGGACCTACGTCCCTAGC         46        15.5511    2.5556     0.8639
69.7305       18     GGGACCTACGTCCCTAGC         46        15.5511    2.5556     0.8639
71.451        18     GGGACCTACGTCCCTAGC         46        15.5511    2.5556     0.8639
69.347        18     GGGACCTACGTCCCTAGC         46        15.5511    2.5556     0.8639
70.173        18     GGGACCTACGTCCCTAGC         46        15.5511    2.5556     0.8639

72.095        19     GGGACCTACGTCCCTAGCC        50        16.8465    2.6316     0.8867
73.8485       19     GGGACCTACGTCCCTAGCC        50        16.8465    2.6316     0.8867
79.0093       19     GGGACCTACGTCCCTAGCC        50        16.8465    2.6316     0.8867
77.682        19     GGGACCTACGTCCCTAGCC        50        16.8465    2.6316     0.8867
77.6783       19     GGGACCTACGTCCCTAGCC        50        16.8465    2.6316     0.8867
86.245        19     GGGACCTACGTCCCTAGCC        50        16.8465    2.6316     0.8867
77.127        19     GGGACCTACGTCCCTAGCC        50        16.8465    2.6316     0.8867

76.4546       20     GGGGACCTACGTCCCTAGCC       55        18.5446    2.75       0.9272
82.822        20     GGGGACCTACGTCCCTAGCC       55        18.5446    2.75       0.9272
75.4015       20     GGGGACCTACGTCCCTAGCC       55        18.5446    2.75       0.9272
78.421        20     GGGGACCTACGTCCCTAGCC       55        18.5446    2.75       0.9272
81.4305       20     GGGGACCTACGTCCCTAGCC       55        18.5446    2.75       0.9272
79.4235       20     GGGGACCTACGTCCCTAGCC       55        18.5446    2.75       0.9272
78.1114       20     GGGGACCTACGTCCCTAGCC       55        18.5446    2.75       0.9272

84.4536       21     GGGACCTACGTCCCTAGCCCC      61        20.9093    2.9048     0.9957
80.505        21     TGGGGACCTACGTCCCTAGCC      60        20.3055    2.8571     0.9669
80.735        21     TGGGGACCTACGTCCCTAGCC      60        20.3055    2.8571     0.9669
80.1095       21     TGGGGACCTACGTCCCTAGCC      60        20.3055    2.8571     0.9669
84.1336       21     TGGGGACCTACGTCCCTAGCC      60        20.3055    2.8571     0.9669
80.4745       21     TGGGGACCTACGTCCCTAGCC      60        20.3055    2.8571     0.9669
80.283        21     TGGGGACCTACGTCCCTAGCC      60        20.3055    2.8571     0.9669

84.4895       22     GGGGACCTACGTCCCCAGCCCC     65        22.7252    2.9545     1.033
83.464        22     GGGGACCTACGTCCCCAGCCCC     65        22.7252    2.9545     1.033
83.626        22     GGGGACCTACGTCCCCAGCCCC     65        22.7252    2.9545     1.033
84.0851       22     GGGGACCTACGTCCCCAGCCCC     65        22.7252    2.9545     1.033
84.3885       22     GGGGACCTACGTCCCCAGCCCC     65        22.7252    2.9545     1.033
84.109        22     GGGGACCTACGTCCCCAGCCCC     65        22.7252    2.9545     1.033
83.362        22     GGGGACCTACGTCCCCAGCCCC     65        22.7252    2.9545     1.033

Total Time = 6340.74538898468
"""
