medidas_de_unidades = ['bit','byte','Kilobyte','megabyte','gigabyte','terabyte','petabyte']

valor_atual = int(input("escolha o valor a ser convertido:"))
unidade_atual = int(input("escolha a unidade de medida:"))
unidade_final = int(input("escolha a unidade final"))


while unidade_atual not in medidas_de_unidades :
    print("Essa unidade não existe, tente novamente!:")
    unidade_atual = input()

while unidade_final not in medidas_de_unidades :
    print("Essa unidade não existe, tente novamente!:")
    unidade_final = input()


def conversao (valor_atual, unidade_atual, unidade_final):
    valor_final = valor_atual
    if unidade_atual == 'bit':
        valor_final = valor_final/8
        unidade_atual = 'byte'


    if medidas_de_unidades.index(unidade_atual) <medidas_de_unidades. index(unidade_final) :
        for i in range (medidas_de_unidades. index (unidade_atual), medidas_de_unidades. index (unidade_final)) :
            valor_final = valor_final/1024


    else:
        for i in range (medidas_de_unidades. index (unidade_atual), medidas_de_unidades. index (unidade_final),-1) :

           valor_final = valor_final *1024

        if unidade_atual == 'bit' :

            valor_final = (valor_final/1024)*8

    print (valor_final)

    conversao(valor_atual, unidade_atual, unidade_final)




