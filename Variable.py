from Tag import Tag


class Variable():
    def __init__(self, name: str):
        self.name: str = name
        self.tags: list[Tag] = []
        self.total: int = 0

# Se cuentan los tags relacionados a la columna con relación a los tags de la query.

    def register(self, fact: str, line: str):
        try:
            tag = next(tag for tag in self.tags if tag.tag == fact)
            tag.registerOcurrence(line)
        except StopIteration:
            tag = Tag(fact)
            tag.registerOcurrence(line)
            self.tags.append(tag)
        self.total += 1


#Se devuelve la totalidad de las ocurrencias  relacionados con un tag de la columna.

    def getOcurrencias(self, ind: str, columna: str):
        for i in range(0, len(self.tags)):
            if self.tags[i] == columna:
                for j in range(0, len(self.Query.tags)):
                    if ind == self.Query.tags[j]:
                        return self.counts[i][j]

    def __str__(self):
        return "{}: {} total:{}".format(
            self.name, '({})'.format(', '.join([str(i) for i in self.tags])),
            str(self.total))

    def __repr__(self):
        return str(self)

    def getProbCond(self, conditionalTag: str, query: Tag,
                    index: int) -> float:
        try:
            tag = next(tag for tag in self.tags if tag.tag == conditionalTag)
            return tag.getProbCond(query, index)
        except StopIteration:
            return 0.0

    def getTag(self, tag: str):
        try:
            return next(ftag for ftag in self.tags if ftag.tag == tag)
        except StopIteration:
            return None
