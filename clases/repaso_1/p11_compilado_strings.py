# Escribe tu código acá :)

data = input()
info = input()

palabra = ''
for i_info in range(len(info)):
    letra = info[i_info]
    if letra == 'O':
        letra_data = data[i_info]
        palabra = palabra+letra_data

print(palabra)