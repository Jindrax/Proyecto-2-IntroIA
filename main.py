from Variable import Variable
from Query import Query

variables = []

#Columna que contiene la información principal de la consulta
solucion=Query("¿Se jugó?",["Si","No" ])


# Se agregan las columans con la información de la cual depende  la solución
variables.append(Variable("Cielo",["Lluvia","Nublado", "Soleado" ], solucion))

variables.append(Variable("Temperatura",["Calor","Templado","Frio" ], solucion))

variables.append(Variable("Humedad",["Alta","Normal", "Baja" ], solucion))

variables.append(Variable("Viento",["Si","No" ], solucion))

#Se extraen los datos y se tiene el conteo de las variables y sus respectvos tags.

fic = open("data.dat", "r")
lines = fic.readlines()
headers = lines.pop(0);


for line in lines:
    data= line.rstrip().split(",")
    last=data.pop()
    solucion.add(last)
    for variable,dat in zip(variables,data):
        variable.add(dat, last)


#Se imprime el query y valores de las variables
print(solucion)
for variable in variables:
  print(variable.counts)

#consulta que se desea desarrollar
consulta=["Lluvia", "Templado", "Normal", "Si" ]


#Se calcula la solución del ejercicio, se calculan las probabilidades tentativas de cada tag del Query

soluciones=[]
for tag, val  in zip (solucion.tags, solucion.counts):
  tent=1
  for variable,dat in zip(variables,consulta):
    tent=tent*variable.getOcurrencias(tag,dat)
  tent=tent/(solucion.total*(val**(len(consulta)-1)))
  soluciones.append([tent])

#print(soluciones)

#Se busca el tag que tenga mayor probabilidad

mayorTag=solucion.tags[0]
mayorValor=soluciones[0]
for tag, val  in zip (solucion.tags, soluciones):
  if(val>mayorValor):
    mayorTag=tag
    mayorValor=val

print("La respuesta es "+mayorTag)
print("Probabilidad: ")
print(mayorValor)