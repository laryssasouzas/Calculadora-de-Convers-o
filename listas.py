brincandocomlista = ['gato', 'gatito', 'gatinhos']

print('minha lista')
print(brincandocomlista)
brincandocomlista.append('gatão')
brincandocomlista.append('cat')
print(brincandocomlista)
#brincandocomlista.pop(1)
print(brincandocomlista)
tempvalue = brincandocomlista [2]
print('escolha a posição para remover um item')
indexPop = int(input())
brincandocomlista.pop(indexPop)
print(brincandocomlista)