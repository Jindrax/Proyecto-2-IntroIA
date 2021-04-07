from IMotor import IMotor

motor = IMotor()

motor.addClause("Hombre(marco)")
motor.addClause("Pompeyano(marco)")
motor.addClause("¬Pompeyano(X3) | Romano(X3)")
motor.addClause("Gobernante(cesar)")
motor.addClause("¬Romano(X5) | ¬Leal(X5, cesar) | Odia(X5, cesar)")
motor.addClause("¬Hombre(X7) | ¬Gobernante(Y7) | ¬IntentaAsesinar(X7, Y7) | Leal(X7, Y7)")
motor.addClause("IntentaAsesinar(marco, cesar)")
motor.query("Odia(marco, cesar)")

input()

motor = IMotor()

motor.addClause('¬Animal(Y1) | ¬Ama(X1, Y1) | Ama(F(X1Y1), X1)')
motor.addClause('¬Animal(G(Z2)) | ¬Mata(F(Z2), G(Z2)) | ¬Ama(Z2, F(Z2))')
motor.addClause('¬Animal(X3) | Ama(jack, X3)')
motor.addClause('Gato(tuna)')
motor.addClause('Mata(jack, tuna) | Mata(curiosidad, tuna)')
motor.addClause('¬Gato(X5) | Animal(X5)')
motor.query('Mata(curiosidad, tuna)')

#print(motor.solve('Animal(X)'))
