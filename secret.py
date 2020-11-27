ref_arquivo = open("arquivo.txt","r")

for linha in ref_arquivo:
    valores = linha.split()
    print('QB ', valores[0], valores[1], 'obteve a avaliacao ', valores[2] )

    host = valores[0].replace(",","")
    print(host)
    user = valores[1].replace(",","")
    print(user)
    password = valores[2].replace(",","")
    print(password)
    db = valores[3].replace(",","")
    print(db)

ref_arquivo.close()



