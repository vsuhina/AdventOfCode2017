import re

class Instruction:
    regex = "(\w+) (\w+) ([\d-]+) if (\w+) ([>=<!]+) ([\d-]+)"

    def __init__(self, input):
        m = re.search(self.regex, input)
        self.register = m[1]
        self.operation = m[2]        
        self.modifyBy = int(m[3])
        self.condRegister = m[4]
        self.condComparison = m[5]
        self.condValue = int(m[6])

    def __str__(self):
        return "{1} {0} by {2} if {3} {4} {5}".format(self.register, self.operation, self.modifyBy, self.condRegister, self.condComparison, self.condValue)

    def cond(self, testValue):
        if self.condComparison == '<':
            return testValue < self.condValue
        elif self.condComparison == '<=':
            return testValue <= self.condValue
        elif self.condComparison == '>':
            return testValue > self.condValue
        elif self.condComparison == '>=':
            return testValue >= self.condValue
        elif self.condComparison == '==':
            return testValue == self.condValue
        elif self.condComparison == '!=':
            return testValue != self.condValue
        else:
            return false

    def modify(self, startValue):
        if self.operation == "inc":
            return startValue + self.modifyBy
        elif self.operation == "dec":
            return startValue - self.modifyBy
        else:
            return startValue

if __name__ == "__main__":
    with open("input.txt") as f:
        instructions = [ Instruction(line) for line in f.readlines()]

    registers = {}

    maxVal = 0

    for i in instructions:
        if i.register not in registers:
            registers[i.register] = 0
        if i.condRegister not in registers:
            registers[i.condRegister] = 0

        if i.cond(registers[i.condRegister]):
            registers[i.register] = i.modify(registers[i.register])
        
        tempMax = max(list(registers.values()))
        
        if tempMax > maxVal:
            maxVal = tempMax

    print(maxVal)