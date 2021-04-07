import re
import copy

class Symbol():
  symbolDefinitionPattern = re.compile(r'(\¬?)([A-Z][a-zA-Z_]*)\(((?:[a-zA-Z0-9()]*,? ?)+)\)')
  
  def __init__(self, line):
    self.symbol = ""   #Nombre o identificador del simbolo
    self.atoms = []    #literales o variables que componen el simbolo.
    self.negated = False    #indica si la expresiónn se encuntra negada.
    self.construct(line)   


# Descompoene la información y la almacena en los atributos de la clase simbolo.
  def construct(self, line: str):
    symbolDef = self.symbolDefinitionPattern.findall(line)[0]
    self.negated = False if symbolDef[0] == '' else True
    self.symbol = symbolDef[1]
    for atom in symbolDef[2].split(','):
      self.atoms.append(atom.strip())


  def __str__(self):
    return "{}{}{}".format('¬' if self.negated else '', self.symbol, '({})'.format(', '.join([i for i in self.atoms])))

  def __repr__(self):
    return str(self)


# Soporta las consultas a la base de conocimiento.

  def solve(self, symbol):
    sol = []
    variable = re.compile(r'[A-Z][a-z0-9]*')
    if symbol.symbol == self.symbol:
      for atomReq, ownAtom in zip(symbol.atoms, self.atoms):
        if variable.match(atomReq) and variable.match(ownAtom) == None:
          sol.append("{}: {}".format(atomReq, ownAtom))
    if len(sol) > 0:
      return(sol)
    else:
      return None

# Realiza el proceso de unifiación. El diccionario permite realizar la traducción de variables a literales.

  def unify(self, unifyVariables: dict):
    newSymbol = copy.deepcopy(self) #Crea una copia de si mismo y  todos sus atributos.
    for index, atom in enumerate(newSymbol.atoms):
      try:
        newSymbol.atoms[index] = unifyVariables[atom]
      except Exception:   #La excepción soporta el caso en el cual no se encuentra el átomo en el diccionario. De esta forma se ignora esta excepción.
        None
    return newSymbol