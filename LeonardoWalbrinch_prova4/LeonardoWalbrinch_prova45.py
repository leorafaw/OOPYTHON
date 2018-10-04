import re
regMaria = re.compile(r'Maria [A-Za-z]{1,}')
regPaulo = re.compile(r'Paulo [A-Za-z]{1,}')
arquivo = open("arquivo.txt","r")

for i in arquivo.readlines():
    if regMaria.findall(i):
        splitado = i.split(",")
        print(splitado[0])
    if regPaulo.findall(i):
        splitado = i.split(",")
        print(splitado[0])