class Variable():
  
  def __init__(self, name,listTags, Query):
    self.name = name
    self.tags = listTags #Inicializar con tags
    self.counts = []
    for i in range (len(listTags)):
      self.counts.append([0]*len(Query.tags))
    self.total = 0
    self.Query = Query


# Se cuentan los tags relacionados a la columna con relación a los tags de la query.
  def add(self, fact: str, ind: str):
    for i in range (0, len(self.tags)):
      if self.tags[i] == fact:
        for j in range (0, len(self.Query.tags)):
          if ind==self.Query.tags[j]:
            self.counts[i][j] =self.counts[i][j]+1
        self.total +=1
    

#Se devuelve la totalidad de las ocurrencias  relacionados con un tag de la columna.

  def getOcurrencias(self,ind: str, columna: str):
    for i in range (0, len(self.tags)):
      if self.tags[i] == columna:
        for j in range (0, len(self.Query.tags)):
          if ind==self.Query.tags[j]:
            return self.counts[i][j]
        


  def __str__(self):
    return "{}{}{}{}{}".format( self.name, '({})'.format(', '.join([i for i in self.tags])), [i for i in self.counts],str(self.total), self.Query.name )

  def __repr__(self):
    return str(self)
