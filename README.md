# Bayesian Network Structure Learning with Breast Cancer Data

Implementation of [libpgm](https://github.com/CyberPoint/libpgm) to estimate the Bayesian Network structure of the [Wisconsin Breast Cancer Database](https://archive.ics.uci.edu/ml/datasets/Breast+Cancer+Wisconsin+(Original)). This code was written by Marc Vidal and Justin Shenk for Nico Potyka's "Basic Methods in Probabilistic Reasoning" seminar.

# Project structure
Python script is located in `libpgm-1.3/implementation/learnthestructure.py`.

The original data is located in `libpgm-1.3/data/breast-cancer-wisconsin.data`.

# Getting started
Clone the repository

`git clone https://github.com/JustinShenk/learnthestructure.git`

Install libpgm package

`cd learnthestructure`

`cd libpgm-1.3`

`[sudo] python setup.py install`

Run the script

`cd implementation`

`python learnthestructure.py [p-value parameter] [# of bins] [lg]`


The data is discrete rather than continuous. To test the binning of the linear Gaussian function, however, add `lg` as an argument and specify the number of bins. By default, p-value threshold is .05 and linear Gaussian data is discretized into 10 bins.

# Data Variables

| No. | Attribute | Domain |
| --- | --- | --- |
| 1. | Sample code number | id number |
| 2. | Clump Thickness | 1 - 10 |
| 3. | Uniformity of Cell Size  | 1 - 10 |
| 4. | Uniformity of Cell Shape | 1 - 10 |
| 5. | Marginal Adhesion | 1 - 10 |
| 6. | Single Epithelial Cell Size  | 1 - 10 |
| 7. | Bare Nuclei | 1 - 10 |
| 8. | Bland Chromatin | 1 - 10 |
| 9. | Normal Nucleoli  | 1 - 10 |
| 10. | Mitoses | 1 - 10 |
| 11. | Class: | (2 for benign, 4 for malignant) |

# Output

This implementation outputs estimated edges and vertices from the data in files marked with optional arguments:
`/data/breast-data-result-0.1-10.txt`

CPDs are produced:
`/data/breast-data-result-CPDs.txt`

Example output is at the bottom.

# Query

Open the python shell from the implementation folder and instantiate the class:
`from learnthestructure import LearnTheStructure`
`bn = LearnTheStructure()`

What is the probability that a patient's cancer is malignant given that Bare Nuclei has a value of 10?

`evidence = dict(BareNuclei=10)`

`query = dict(Class=[4])`

`bn.query_it(evidence,query)`

`The probability of  {'Class': [4]}  given  {'BareNuclei': 10}  is  0.808146976884`


```
Edges:
[
  [
    "UniformityofCellShape",
    "UniformityofCellSize"
  ],
  [
    "UniformityofCellSize",
    "Class"
  ],
  [
    "BareNuclei",
    "Class"
  ]
]
```
```
Vertices data with CPD:
{
  "SingleEpithelialCellSize": {
    "vals": [
      2,
      7,
      3,
      1,
      6,
      4,
      5,
      8,
      10,
      9
    ],
    "numoutcomes": 10,
    "cprob": [
      0.5522174535050072,
      0.017167381974248927,
      0.10300429184549356,
      0.06723891273247497,
      0.058655221745350504,
      0.06866952789699571,
      0.055793991416309016,
      0.030042918454935622,
      0.044349070100143065,
      0.002861230329041488
    ],
    "parents": [],
    "children": []
  },
  "UniformityofCellSize": {
    "vals": [
      1,
      4,
      8,
      10,
      2,
      3,
      7,
      5,
      6,
      9
    ],
    "numoutcomes": 10,
    "cprob": [
      0.5493562231759657,
      0.05722460658082976,
      0.04148783977110158,
      0.09585121602288985,
      0.06437768240343347,
      0.07439198855507868,
      0.027181688125894134,
      0.04291845493562232,
      0.03862660944206009,
      0.008583690987124463
    ],
    "parents": [],
    "children": [
      "UniformityofCellShape",
      "Class"
    ]
  },
  "BareNuclei": {
    "vals": [
      1,
      10,
      2,
      4,
      3,
      9,
      7,
      5,
      8,
      6
    ],
    "numoutcomes": 10,
    "cprob": [
      0.597997138769671,
      0.1888412017167382,
      0.04291845493562232,
      0.027181688125894134,
      0.04005722460658083,
      0.012875536480686695,
      0.011444921316165951,
      0.04291845493562232,
      0.030042918454935622,
      0.005722460658082976
    ],
    "parents": [],
    "children": [
      "Class"
    ]
  },
  "UniformityofCellShape": {
    "vals": [
      1,
      4,
      8,
      10,
      2,
      3,
      5,
      6,
      7,
      9
    ],
    "numoutcomes": 10,
    "cprob": {
      "['1']": [
        0.8619791666666666,
        0.013020833333333334,
        0.0,
        0.0,
        0.06770833333333333,
        0.057291666666666664,
        0.0,
        0.0,
        0.0,
        0.0
      ],
      "['8']": [
        0.0,
        0.06896551724137931,
        0.3793103448275862,
        0.06896551724137931,
        0.0,
        0.034482758620689655,
        0.0,
        0.06896551724137931,
        0.27586206896551724,
        0.10344827586206896
      ],
      "['3']": [
        0.17307692307692307,
        0.15384615384615385,
        0.019230769230769232,
        0.0,
        0.21153846153846154,
        0.25,
        0.1346153846153846,
        0.057692307692307696,
        0.0,
        0.0
      ],
      "['6']": [
        0.0,
        0.2222222222222222,
        0.037037037037037035,
        0.037037037037037035,
        0.0,
        0.07407407407407407,
        0.14814814814814814,
        0.3333333333333333,
        0.1111111111111111,
        0.037037037037037035
      ],
      "['10']": [
        0.0,
        0.029850746268656716,
        0.08955223880597014,
        0.7164179104477612,
        0.014925373134328358,
        0.029850746268656716,
        0.029850746268656716,
        0.029850746268656716,
        0.04477611940298507,
        0.014925373134328358
      ],
      "['7']": [
        0.0,
        0.10526315789473684,
        0.2631578947368421,
        0.15789473684210525,
        0.0,
        0.0,
        0.05263157894736842,
        0.05263157894736842,
        0.3157894736842105,
        0.05263157894736842
      ], ...
}
```
