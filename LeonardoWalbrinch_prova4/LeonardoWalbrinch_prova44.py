import re
regex = re.compile(r'(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[%,$,#,@]+)(?=^.{4,}$)')
senha = input("Informe sua senha: ")
if regex.match(senha):
    print("SENHA FORTE")
else:
    print("SENHA FRACA")