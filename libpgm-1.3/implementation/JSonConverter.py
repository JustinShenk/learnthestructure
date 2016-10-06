'''
   #  Attribute                     Domain
   -- -----------------------------------------
   1. Sample code number            id number
   2. Clump Thickness               1 - 10
   3. Uniformity of Cell Size       1 - 10
   4. Uniformity of Cell Shape      1 - 10
   5. Marginal Adhesion             1 - 10
   6. Single Epithelial Cell Size   1 - 10
   7. Bare Nuclei                   1 - 10
   8. Bland Chromatin               1 - 10
   9. Normal Nucleoli               1 - 10
  10. Mitoses                       1 - 10
  11. Class:                        (2 for benign, 4 for malignant)

'''
from collections import OrderedDict  # custom-array sorting
import json  # JSON formatting

# Define attributes
attributes = [
    "Sample code number",
    "Clump Thickness",
    "Uniformity of Cell Size",
    "Uniformity of Cell Shape",
    "Marginal Adhesion",
    "Single Epithelial Cell Size",
    "Bare Nuclei",
    "Bland Chromatin",
    "Normal Nucleoli",
    "Mitoses",
    "Class"
]
data = []  # List initialization

with open("../data/breast-cancer-wisconsin.data", "r") as document:
    for line in document:
        # Comma-defined splitting of line
        values = line.split(",")
        # Remove the line return character "\n"
        values[-1] = values[-1].strip()
        if not line:
            continue
        # Add to every defined index its correspondant value
        data.append({a: v for a, v in zip(attributes, values)})

# Order the data using our attributes definition
ordered_data = [OrderedDict(sorted(item.iteritems(), key=lambda (k, v): attributes.index(k))) for item in data]

# Write the data to JSON format
with open('../data/breastdata.txt', 'w') as outfile:
    json.dump(ordered_data, outfile, indent=2, sort_keys=False,
              separators=(',', ': '))
