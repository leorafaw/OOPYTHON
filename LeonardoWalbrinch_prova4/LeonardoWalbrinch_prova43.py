import re
regCPF = re.compile(r'\d\d\d.\d\d\d.\d\d\d-\d\d')
regEmail = re.compile(r'([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+)',re.VERBOSE)

arquivo = open("arquivo.txt","r")

for i in arquivo.readlines():
    matchCPF=regCPF.findall(i)
    matchEmail=regEmail.findall(i)
    print(matchCPF, matchEmail)
