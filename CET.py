n = 'condição de existencia de triângulos'
print(n)
print('---'*10)
print('Triângulos'.upper())
print('---'*10)
a = float(input('Primeiro lado: '))
b = float(input('Segundo lado: '))
c = float(input('Terceiro lado: '))
maior = a
if b + a < c:
  maior = c
if a + c < b:
  maior = b
if c + b < a:
  maior = a
  print('Existe a comdição')
else:
  print('Não existe a condição')
