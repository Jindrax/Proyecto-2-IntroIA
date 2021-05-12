from Motor import Motor

motor = Motor()
motor.loadData("data.dat")
motor.print()
query = "Cielo: Lluvia, Temperatura: Templado, Humedad: Normal, Viento: Si > Jugo"
motor.query(query)