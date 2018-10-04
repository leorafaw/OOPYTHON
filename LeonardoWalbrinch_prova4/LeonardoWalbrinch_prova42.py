import re
regData = re.compile(r'\d\d/\d\d/\d\d\d\d')
regCep = re.compile(r'\d\d\d\d\d-\d\d\d')

frase = "data = 30/08/2018 e CEP = 93800-000"
matchCep = regCep.findall(frase)
matchData = regData.findall(frase)

print("CEPs: ", matchCep, "Datas: ", matchData)