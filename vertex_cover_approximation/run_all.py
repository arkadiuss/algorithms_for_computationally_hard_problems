import os
import sys

graphs = [
"e5",
"e10",
"e20",
"e40",
"s25",
"s50",
"b20",
"b30",
"f30",
"f35",
"f40",
"f56",
"m20",
"m30",
"m40",
"m50",
"p20",
"p35",
"p200",
"r30_01",
"r30_05",
"r50_001",
"r50_01",
"r50_05",
"p60",
"p150",
"r100_005",
"r100_01",
"r200_001",
"r200_005",
"b100",
"m100",
"p150",
"e150",
"k330_a",
"k330_b",
"k330_c",
"k330_d",
"k330_e",
"k330_f",
"s500"
]

for i,g in enumerate(graphs):
    print("{0}/{1} {2}".format(i+1, len(graphs), g))
    os.system("python3.6 {0} graph/{1}".format(sys.argv[1], g))
