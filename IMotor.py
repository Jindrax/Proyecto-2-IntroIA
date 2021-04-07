from Clause import Clause
from Symbol import Symbol
from PQueue import PQueue


#Clase encargada de realizar el proceso de prueba por resolución.
class IMotor():
    def __init__(self):
        self.clauses = []  #lista de clausulas

#Permite agregar una nueva clausula

    def addClause(self, line: str):
        self.clauses.append(Clause(line))

#Permite consultar la base de conocimiento

    def solve(self, line: str):
        request = Symbol(line)
        sol = None
        for clause in self.clauses:
            sol = clause.solve(request)
            if sol != None:
                return (sol)
        return (None)

#Permite verificar si una expresión es verdadera por prueba de resolución.

    def query(self, line: str):
        symbolQuery = Symbol(line)
        symbolQuery.negated = not symbolQuery.negated
        result = self.recursiveQuery([symbolQuery])
        print("The query {} is {}".format(line, not result))


#Permite eliminar la expresiones que se cancelan dentro de la clausula.

    def sanitizeQuery(self, query):
        sanitizedQuery = []
        for symbol in query:
            valid = True
            for symbolB in query:
              #buscar un simbolo posible con el que se pueda cancelar y marcarlo como invalido.  
                if symbol.symbol == symbolB.symbol:
                    if symbol.atoms == symbolB.atoms:
                        if symbol.negated != symbolB.negated:
                            valid = False
            if valid:
                sanitizedQuery.append(symbol)
        return sanitizedQuery


#Permite observar las iteraciones del proceso de prueba por resolución.

    def printIteration(self, query, unifiedClause, newQuery):
        print('[{}] + \n\t[{}] -> \n\t\t[{}]\n'.format(' | '.join([str(i) for i in query]), ' | '.join([str(j) for j in unifiedClause]), ' | '.join([str(k) for k in newQuery])))


#Es el eje principal de la clase IMotor, permite realizar todo el proceso de prueba por resolución.

    def recursiveQuery(self, query):
        #input()
        if len(query) == 0:
            return False
        else:
            pq = PQueue()
            #Obtinene todos las cluasulas que pueden ser unificables con un determinado simbolo dentro de la consuta. 
            for symbol in query:
                for clause in self.clauses:
                    solVal = clause.isThereInvertedSymbol(symbol)
                    if solVal > 0:
                        pq.insert((solVal, clause, symbol))
            while not pq.isEmpty():
                elected = pq.delete()
                #Unificación del escenario mas prometedor.
                unifiedClause = elected[1].unify(elected[2])
                #Seeliminan las expresiones no necesarias.
                newQuery = self.sanitizeQuery(query + unifiedClause)
                self.printIteration(query, unifiedClause, newQuery)
                #Se continua el proceso sobre el resto de la expresión.
                solved = self.recursiveQuery(newQuery)
                if not solved:
                    return solved
            return True
