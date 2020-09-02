#Variables
p1 = 0
p2 = 0
v = float(input('Ingresa el volúmen en litros: '))
n = float(input('Ingresa los moles: '))
r = 0.0821
t = float(input('Ingresa la temperatura en Kelvin: '))
a = float(input('Ingresa la "a": '))
b = float(input('Ingresa la "b": '))

# Formulas
p1 = (n * r * t) / v

p2 = ((n * r * t) / (v - (n * b))) - ((a * (n ** 2))/(v ** 2))

pf = p1 - p2

print('La presión 1 es: ' + str(p1))
print('La presión 2 es: ' + str(p2))
print('La diferencia de presión es: ' + str(pf))

    
