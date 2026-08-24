import math
angulo_graus = float (input('digite um angulo qualquer: '))
angulo_radianos = math.radians (angulo_graus)

seno = math.sin (angulo_radianos)
cosseno = math.cos (angulo_radianos)
tangente = math.tan (angulo_radianos)

print (f'Para o ângulo de {angulo_graus}°')
print (f'O Seno é {seno:.2f}')
print (f'O Cosseno de {cosseno:.2f}')
print (f'O Tangente de {tangente:.2f}')
