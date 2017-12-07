import re
from collections import Counter

class Node:
    regex = "(([a-z])*) \((\d+)\)(?:( -> )([a-z, ]*))?"

    def __init__(self, inp):
        m = re.search(self.regex, inp)
        self.name = m.group(1)
        self.weight = int(m.group(3))
        self.totalweight = None
        if m.group(5) is not None:
            self.children = m.group(5).split(', ')
        else:
            self.children = []
        self.parent = None
        self.isBalanced = None

    def __str__(self):
        if self.children:
            return "{0} ({1}/{2}) -> {3} Balanced: {4}".format(self.name, self.weight, self.totalweight, self.children, self.isBalanced)
        else:
            return "{0} ({1})".format(self.name, self.weight)
        

def calcTotal(dict, node):
    if len(node.children) == 0:
        dict[node.name].totalweight = node.weight
        dict[node.name].isBalanced = True
        return dict[node.name].totalweight
    else:
        weights = [calcTotal(dict, dict[c]) for c in node.children]
        dict[node.name].isBalanced = len(set(weights)) == 1
        dict[node.name].totalweight = node.weight + sum(weights)
        return dict[node.name].totalweight


if __name__ == "__main__":
    
    with open("input.txt") as f:
        nodes = [Node(l.strip()) for l in f.readlines()]

        dict = {}

        for n in nodes:
            dict[n.name] = n

        for n in nodes:
            for c in n.children:
                dict[c].parent = n.name

        for d in dict.values():
            if d.parent is None:                
                root = d
                break

        print("***")
        print(root)

        calcTotal(dict, root)

        for node in dict.values():
            if not node.isBalanced:
                print("***")
                print(node)

        print("***")
        node = dict["zuahdoy"]
        print(node)
        for c in node.children:
            print(dict[c])

        print("***")

        node = dict["mfzpvpj"]
        print(node)
        for c in node.children:
            print(dict[c])

       

        
        
       




    
    


