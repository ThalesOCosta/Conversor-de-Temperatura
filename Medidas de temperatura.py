# C -> F
c = float(input('Celsius: '))
f = c * (9/5) + 32
print(f'Fahrenheit: {f}')

# F -> C
f = float(input('Fahrenheit: '))
c = 5 * (f - 32) / 9
print(f'Celsius: {c}')

# C -> K
c = float(input('Celsius: '))
k = c - 273.15
print(f'Kelvin: {k}')

# K -> C
k = float(input('Kelvin: '))
c = k + 273.15
print(f'Celsius: {c}')
