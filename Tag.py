class Tag:
  def __init__(self, tag:str):
    self.tag:str = tag
    self.count:int = 0
    self.ocurrences:list[str] = []
  
  def getProb(self, total) -> float:
    return self.count/total

  def registerOcurrence(self, line):
    self.count += 1
    self.ocurrences.append(line)

  def getProbCond(self, tag, index:int) -> float:
    local = 0
    for ocurrence in self.ocurrences:
      splited = ocurrence.split(",")
      if splited[index].strip() == tag.tag:
        local += 1
    return local/tag.count

  def __str__(self):
    return "{}:{}".format( self.tag, self.count)

  def __repr__(self):
    return str(self)