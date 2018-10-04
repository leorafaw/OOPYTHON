import re
regexPlaca = re.compile(r'\D\D\D-\d\d\d\d')
frase = input("Informe uma placa de carro válida, no formato: (XXX-XXXX) ")
match = regexPlaca.findall(frase)
print(match)