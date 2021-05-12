from Variable import Variable


class Motor:
    def __init__(self):
        self.variables: list[Variable] = []

    def loadData(self, file: str):
        fic = open(file, "r")
        lines = fic.readlines()
        headers = lines.pop(0)
        for header in headers.split(","):
            self.variables.append(Variable(header.strip()))
        for line in lines:
            for index, variable in enumerate(line.split(",")):
                self.variables[index].register(variable.strip(), line)

    def print(self):
        for variable in self.variables:
            print(variable)

    def getVariable(self, variable: str):
        try:
            return next(fvariable for fvariable in self.variables
                        if fvariable.name == variable)
        except StopIteration:
            return None

    def query(self, query: str):
        print("For query: " + query + ":")
        parsedQuery = query.split(">")
        knownVariables = parsedQuery[0].split(",")
        question = parsedQuery[1].strip()
        for index, variable in enumerate(self.variables):
            if variable.name == question:
                for questionTag in variable.tags:
                    tagProb = questionTag.getProb(variable.total)
                    for knownVariable in knownVariables:
                        knownVariableComp = knownVariable.split(":")
                        tagProb *= self.getVariable(
                            knownVariableComp[0].strip()).getProbCond(
                                knownVariableComp[1].strip(), questionTag,
                                index)
                    print("\t- " + questionTag.tag + " = " + str(tagProb))
