import math
cateto_oposto = float (input('qual o seu cateto oposto?'))
cateto_adjacente = float (input('qual o seu cateto adjacente?'))

hipotenusa = math.hypot(cateto_oposto, cateto_adjacente)

print(f' a hipotenusa vai medir {hipotenusa:.2f}')