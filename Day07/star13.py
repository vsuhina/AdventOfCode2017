import re

class Node:
    regex = "(([a-z])*) \((\d+)\)(?:( -> )([a-z, ]*))?"

    def __init__(self, inp):
        m = re.search(self.regex, inp)
        self.name = m.group(1)
        self.weight = int(m.group(3))
        if m.group(5) is not None:
            self.children = m.group(5).split(', ')
        else:
            self.children = []
        self.parent = None

    def __str__(self):
        if self.children:
            return "{0} ({1}) -> {2}".format(self.name, self.weight, self.children)
        else:
            return "{0} ({1})".format(self.name, self.weight)
        

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
                print(d.name)
                break



    
    


