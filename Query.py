class Query():
  
  def __init__(self, name,listTags):
    self.name = name
    self.tags = listTags #tags de la columna
    self.counts = [0]* len(listTags)
    self.total = 0


#Se cuentan los tags relacionados al query.

  def add(self, fact: str):

    for i in range (0, len(self.tags)):
      if self.tags[i] == fact:
        self.counts[i] +=1
        self.total +=1
    
  def __str__(self):
    return "{}{}{}{}".format( self.name, '({})'.format(', '.join([i for i in self.tags])), [i for i in self.counts],str(self.total))

  def __repr__(self):
    return str(self)