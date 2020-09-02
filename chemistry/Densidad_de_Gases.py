#Variables
d = input('Ingresa la densidad, si no sabes pon "x": ')
p = input('Ingresa la presión, si no sabes pon "x": ')
m = input('Ingresa la masa, si no sabes pon "x": ')
r = 0.0821
t = input('Ingresa la temperatura en kelvin, si no sabes pon "x": ')

#Formulas
if d == "x":
    d = (float(p) * float(m)) / (float(r) * float(t))
    print('La densidad es: ' + str(d) + ' g/l')
    
if p == "x":
    p = (float(r) * float(t) * float(d)) / float(m)
    print('La presión es: ' + str(p) + ' atm ó mmHg')

if m == "x":
    m = (float(r) * float(t) * float(d)) / float(p)
    print('La masa es: ' + str(m) + ' g')
    
if t == "x":
    t = (float(m) * float(p)) / (float(r) * float(t) * float(d))
    print('La temperatura es: ' + str(t) + ' K')
