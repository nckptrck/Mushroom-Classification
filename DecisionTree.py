from Matrix import Matrix
class DecisionTree:

    def __init__(self) -> None:
        pass

    def main(self):
        self.process_file("/Users/nicholaspatrick/Desktop/RandomForest/Mushroom-Classification/Data/agaricus-lepiota.data")

    def process_file(self, fname):
        file = open(fname, "r")
        data = []
        for line in file:
            parts = line.strip().split(",")
            # Remove the 11th feature de to missing values
            #keep_features = parts[1:11] + parts[12:]

            # for testing
            keep_features = parts[:5]
            data.append(keep_features)
        
        r = -1
        c = -1
        for line in data:
            r += 1
            for num in line:
                c += 1
                p = num.split(".")
                data[r][c] = p[0]
            c = -1

        
        print(data)

        
        return data

    
    def print_decision_tree(self,data, attributes, rows, level, current_igr):
        m = Matrix(data)
        if m.find_entropy(rows=rows) == 0:
            for _ in range(level):
                print("\t", end="")
            print("Value = " + str(m.find_most_common_value(rows)))
            return
        if len(rows) < 16:
            for _ in range(level):
                print("\t", end="")
            print("Value = " + str(m.find_most_common_value(rows)))
            return

        if not attributes or not rows:
            for _ in range(level):
                print("\t", end="")
            print("Value = " + str(m.find_most_common_value(rows)))
            return

        split_attr = -1
        max_gain = 0.0

        for attr in attributes:
            igr = m.find_gain_ratio(attr, rows)
            #print("attr: ",attr, "igr: ", igr, "max gain: ", max_gain)
            if igr > max_gain and igr > 0.01:
                max_gain = igr
                split_attr = attr
        
        #print(abs(max_gain - current_igr))
        if abs(max_gain - current_igr) < 0.01:
            for _ in range(level):
                print("\t", end="")
            print("Value = " + str(m.find_most_common_value(rows)))
            return

        if split_attr != -1:
            #print("SPLIT ATTR: ", split_attr, "\nGAIN: ", max_gain, "\n Last Gain:", current_igr)
            split_data = m.split(split_attr, rows)
            attr_subset = attributes.copy()
            attr_subset.remove(split_attr)

            for key, subset_rows in split_data.items():
                for _ in range(level):
                    print("\t", end="")
                print(f"If attribute {split_attr+1} has value {key}")
                if not attr_subset or abs(max_gain - current_igr) < 0.01:
                    for _ in range(level + 1):
                        print("\t", end="")
                    print("Value = " + str(m.find_most_common_value(subset_rows)))
                else:
                    self.print_decision_tree(data, attr_subset, subset_rows, level + 1, max_gain)
        else:
            for _ in range(level):
                print("\t", end="")
            print("Value = " + str(m.find_most_common_value(rows)))
            return






dt = DecisionTree()

d = dt.process_file("/Users/nicholaspatrick/Desktop/RandomForest/Mushroom-Classification/Data/testData.txt")


dt.print_decision_tree(d, [0,1,2,3], [i for i in range(0,150)], 0, 100)
    