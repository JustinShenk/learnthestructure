# Bayesian Structure Learning with Breast Cancer Data
Implementation of [libpgm](https://github.com/CyberPoint/libpgm) to estimate the Bayesian Network structure of the [Wisconsin Breast Cancer Database](https://archive.ics.uci.edu/ml/datasets/Breast+Cancer+Wisconsin+(Original))

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

`python learnthestructure.py`

# Output
This implementation outputs estimated edges and vertices from the data:

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

Vertices with variance and mean:
{
  "SingleEpithelialCellSize": {
    "mean_base": 3.2160228898426322,
    "parents": [],
    "children": [],
    "mean_scal": [],
    "variance": 4.896109504483208
  },
  "UniformityofCellSize": {
    "mean_base": 0.14785300560650477,
    "parents": [
      "UniformityofCellShape"
    ],
    "children": [
      "Class"
    ],
    "mean_scal": [
      0.9311555526677312
    ],
    "variance": 1.6510156913512928
  },
  "BareNuclei": {
    "mean_base": 3.4864091559370531,
    "parents": [],
    "children": [
      "Class"
    ],
    "mean_scal": [],
    "variance": 13.099600696682977
  },
  "UniformityofCellShape": {
    "mean_base": 3.207439198855508,
    "parents": [],
    "children": [
      "UniformityofCellSize"
    ],
    "mean_scal": [],
    "variance": 8.819629922984193
  },
  "ClumpThickness": {
    "mean_base": 4.4177396280400574,
    "parents": [],
    "children": [],
    "mean_scal": [],
    "variance": 7.917052973694279
  },
  "NormalNucleoli": {
    "mean_base": 2.866952789699571,
    "parents": [],
    "children": [],
    "mean_scal": [],
    "variance": 9.311339927671044
  },
  "Mitoses": {
    "mean_base": 1.5894134477825466,
    "parents": [],
    "children": [],
    "mean_scal": [],
    "variance": 2.937284205312719
  },
  "Samplecodenumber": {
    "mean_base": 1071704.0987124464,
    "parents": [],
    "children": [],
    "mean_scal": [],
    "variance": 380262351292.2461
  },
  "MarginalAdhesion": {
    "mean_base": 2.8068669527896994,
    "parents": [],
    "children": [],
    "mean_scal": [],
    "variance": 8.141526521640355
  },
  "Class": {
    "mean_base": 1.7711888325766989,
    "parents": [
      "UniformityofCellSize",
      "BareNuclei"
    ],
    "children": [],
    "mean_scal": [
      0.12788986630325611,
      0.15074002822813881
    ],
    "variance": 0.18590065989184848
  },
  "BlandChromatin": {
    "mean_base": 3.4377682403433476,
    "parents": [],
    "children": [],
    "mean_scal": [],
    "variance": 5.937114332553557
  }
}
