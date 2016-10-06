import sys
import json
from libpgm.pgmlearner import PGMLearner
from collections import OrderedDict
# Add to PYTHONPATH
sys.path.append("../")


class LearnTheStructure(object):
    """Learns the structure and parameters of linear gaussian model given only the data."""

    def __init__(self):
        self.data = self.clean_data()
        self.estimate_lg_model(self.data)

    def run(self):
        print "[Wisconsin Breast Cancer Dataset Bayesian structure learning with libpgm 1.3]"

    def clean_data(self):
        """Converts raw data to libpgm readable JSON and saves the file."""
        raw_data_path = '../data/breast-cancer-wisconsin.data'
        self.define_attributes()
        data = self.convert_to_json(raw_data_path)

        # Loads and cleans the data.
        data_path = '../data/breast-data.txt'
        f = open(data_path, 'r')
        ftext = f.read()
        ftext = ftext.translate(None, '\t\n ')
        ftext = ftext.replace(':', ': ')
        ftext = ftext.replace(',', ', ')
        ftext = ftext.replace('None', 'null')
        # Imputes missing values with hardcoded median value.
        ftext = ftext.replace('?', '1')
        data = json.loads(ftext)
        f.close()

        # Converts unicode strings to int data type.
        clean_data = []
        for d in data:
            clean_data.append(dict((k, int(v)) for k, v in d.iteritems()))

        # Outputs imputed data.
        with open('../data/breast-data-imputed.txt', 'w') as out_file:
            json.dump(clean_data, out_file, indent=2, sort_keys=False,
                      separators=(',', ': '))
        return clean_data

    def define_attributes(self):
        self.attributes = [
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

    def convert_to_json(self, path):
        """Converts raw data to json with ordered attributes as keys."""
        json_data = []

        with open(path, "r") as document:
            for line in document:
                values = line.split(",")
                # Remove the line return character "\n"
                values[-1] = values[-1].strip()
                if not line:
                    continue
                json_data.append(
                    {a: v for a, v in zip(self.attributes, values)})

        ordered_data = [OrderedDict(sorted(item.iteritems(), key=lambda (k, v): self.attributes.index(k))) for item in json_data]
        with open('../data/breast-data.txt', 'w') as out_file:
            json.dump(ordered_data, out_file, indent=2, sort_keys=False,
                      separators=(',', ': '))
        return json_data

    def estimate_lg_model(self, data):
        """Estimates the structure and parameters of linear guassian model.

        Args:
            data: A JSON-style list of dictionaries representing instances.

        Returns:
            A libpgm object containing structure, parameters and CPD.
        """
        learner = PGMLearner()
        resultlg = learner.lg_estimatebn(data)

        print "Edges:"
        print json.dumps(resultlg.E, indent=2)
        print "Vertices and CPD:"
        print json.dumps(resultlg.Vdata, indent=2)
        return resultlg

if __name__ == '__main__':
    LearnTheStructure().run()
