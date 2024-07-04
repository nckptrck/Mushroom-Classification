import math

class Matrix:

    def __init__(self, data) -> None:
        self.data = data

    
    def find_frequency(self, attr, value, rows):
        count =  0
        for r in rows:
            if self.data[r][attr] == value:
                count += 1
        return count
    

    def find_different_values(self, attr, rows):
        valueSet = set()
        for r in rows:
            valueSet.add(self.data[r][attr])
        
        return valueSet
    

    def find_rows(self, attr, value, rows):
        found = []
        for r in rows:
            if self.data[r][attr] == value:
                found.append(r)
        return found
    

    def find_entropy(self,rows):
        valueSet = self.find_different_values(4,rows)
        valCount = {}
        for v in valueSet:
            #valCount[v] = self.find_frequency(0,v,rows)
            #for testing
            valCount[v] = self.find_frequency(4,v,rows)
        
        total = len(rows)
        entropy = 0.0

        for v in valueSet:
            n = (valCount[v] * 1.0) / total
            if n == 0:
                entropy += 0
            else:
                entropy += -(n) * math.log2(n)

        return entropy
    

    def find_partitioned_entropy(self,attr, rows):
        valueSet = self.find_different_values(attr,rows)
        totalEntropy = 0.0

        for v in valueSet:
            subset = self.find_rows(attr, v, rows)
            subsetEntropy = self.find_entropy(subset)
            #print("subset E:", subsetEntropy)

            totalEntropy += ((len(subset) * 1.0) / len(rows)) * subsetEntropy
        
        #print("P ENTROPY:", totalEntropy)
        return totalEntropy
    
    def find_information_gain(self,attr, rows):
        initialEntropy = self.find_entropy(rows)
        splitEntropy = self.find_partitioned_entropy(attr, rows)
        #print("IG:", initialEntropy - splitEntropy)
        return initialEntropy - splitEntropy
    
    def find_gain_ratio(self,attr, rows):
        ig = self.find_information_gain(attr, rows)
        denom = 0.0
        total = len(rows)
        valueSet = self.find_different_values(attr, rows)
        valCounts = {}

        for v in valueSet:
            valCounts[v] = self.find_frequency(attr, v, rows)
        
        for i in valCounts.values():
            n = (i * 1.0)/ total
            denom += -n * math.log2(n)

        if denom == 0.0:
            return 0.0
        
        return ig / denom
    
    def find_most_common_value(self,rows):
        valueSet = self.find_different_values(4, rows)
        valueCounts = {}

        for v in valueSet:
            #valueCounts[v] = self.find_frequency(0,v,rows)
            #for testing
            valueCounts[v] = self.find_frequency(4,v,rows)

        mcv = None
        maxCount = 0

        for key in valueCounts:
            if valueCounts[key] > maxCount:
                mcv = key
                maxCount = valueCounts[key]
        
        return mcv
    
    def split(self,attr, rows):
        rMap = {}
        valueSet = self.find_different_values(attr, rows)

        for v in valueSet:
            rList = self.find_rows(attr, v, rows)
            rMap[v] = rList

        return rMap



