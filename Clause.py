import re
from Symbol import Symbol
class Clause():
  symbolExtractionPattern = re.compile(r'\¬?[A-Z][a-zA-Z_]*\((?:[a-zA-Z0-9()]*,? ?)+\)')
  variablePattern = re.compile(r'[A-Z][a-z0-9]*')
  
  def __init__(self, line: str):
    self.symbols = []   #lista de simbolos que componen la clausula
    self.construct(line)

#Permite identificar y almacenar los simbolos de la clausula.

  def construct(self, line: str):
    for symbol in self.symbolExtractionPattern.findall(line):
      self.symbols.append(Symbol(symbol))


  def __str__(self):
    return ' | '.join([str(i) for i in self.symbols])

  def __repr__(self):
    return str(self)

  # permite imprimir los simbolos dentro de la clausula

  def print(self):
    print("Symbols:")
    for symbol in self.symbols:
      print(symbol)

# Soportar las busquedas a la base de conocimiento.

  def solve(self, reqSymbol:Symbol):
    allSol = []
    for symbol in self.symbols:
      sol = symbol.solve(reqSymbol)
      if sol != None:
        allSol.append(sol)
    if len(allSol) > 0:
      return allSol
    return None

#Encuentra una clausula para poder realizar el proceso de unificación. Reviza si los simbolos y los atomos son congruentes.

  def isThereInvertedSymbol(self, symbol:Symbol):
    for ownSymbol in self.symbols:
      #revisa congruencia del simbolo
      if ownSymbol.symbol == symbol.symbol:
        if ownSymbol.negated != symbol.negated:
          invalidAtom = False
           #revisa congruencia de los atomos.
          for ownAtom, symbolAtom in zip(ownSymbol.atoms, symbol.atoms):
            if self.variablePattern.match(ownAtom) == None:
              if ownAtom != symbolAtom:
                invalidAtom = True
          if not invalidAtom:
            return len(self.symbols) #Retorna el tamaño.
    return -1 #Retorna -1.

#Encuentra una clausula para poder realizar el proceso de unificación. Reviza si los simbolos y los atomos son congruentes.

  def findInvertedSymbol(self, symbol:Symbol)->Symbol:
    for ownSymbol in self.symbols:
      if ownSymbol.symbol == symbol.symbol:
        if ownSymbol.negated != symbol.negated:
          invalidAtom = False
          for ownAtom, symbolAtom in zip(ownSymbol.atoms, symbol.atoms):
            if self.variablePattern.match(ownAtom) == None:
              if ownAtom != symbolAtom:
                invalidAtom = True
          if not invalidAtom:
            return ownSymbol  
    return None

#Realiza el proceso de unifiación. Crea el diccionario y delega la unificación al simbolo.

  def unify(self, symbol: Symbol):
    ownSymbol = self.findInvertedSymbol(symbol)
    atomsToUnify = {} #diccionario en blanco
    unifiedSymbols = [] # 
    for atomToUnify, unifiedAtom in zip(ownSymbol.atoms, symbol.atoms):
      #correspondencias de los diccionarios
      atomsToUnify[atomToUnify] = unifiedAtom

    for symbolToUnify in self.symbols:
      unifiedSymbol = symbolToUnify.unify(atomsToUnify)
      unifiedSymbols.append(unifiedSymbol)
    return unifiedSymbols
