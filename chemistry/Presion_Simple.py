#Variables
p = input('Ingresa la presión, si no sabes pon "x": ')
v = input('Ingresa el volumen, si no sabes pon "x": ')
n = input('Ingresa los moles, si no sabes pon "x": ')
r = 0.0821
t = input('Ingresa la temperatura en kelvin, si no sabes pon "x": ')

#Formulas
if p == "x":
    p = (float(n) * float(r) * float(t)) / float(v)
    print('La presión es: ' + str(p) + ' atm o mmHg')
    
if v == "x":
    v = (float(n) * float(r) * float(t)) / float(p)
    print('El volumen es: ' + str(p) + ' litros')
    
if n == "x":
    n = (float(p) * float(v)) / (float(r) * (float(t)))
    print('Los moles son: ' + str(p) + ' moles')
    
if t == "x":
    t = (float(p) * float(v)) / (float(n) * (float(r)))
    print('La temperatura es: ' + str(p) + ' kelvin')