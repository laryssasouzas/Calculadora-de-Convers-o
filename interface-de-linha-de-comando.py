from projeto import converterStringParaFloat, BitParaByte, ByteParaBit, ByteParaKiloByte, KilobyteParaByte, KiloByteParaMegaByte, MegaByteParaKiloByte, MegaByteParaGigaByte, GigaByteParaMegaByte, GigaByteParaTeraByte, TeraByteParaGigaByte, TeraByteParaPetaByte, PetaByteParaTeraByte 

from projeto import converterStringParaFloat, BitParaByte, ByteParaBit, ByteParaKiloByte, KilobyteParaByte, KiloByteParaMegaByte, MegaByteParaKiloByte, MegaByteParaGigaByte, GigaByteParaMegaByte, GigaByteParaTeraByte, TeraByteParaGigaByte, TeraByteParaPetaByte, PetaByteParaTeraByte 
print('-Escreva 1 BitParaByte \n -Escreva 2 ByteParaBit \n -Escreva 3 ByteParaKiloByte \n -Escreva 4 KilobyteParaByte \n -Escreva 5 KiloByteParaMegaByte \n -Escreva 6 MegaByteParaKiloByte \n -Escreva 7 MegaByteParaGigaByte \n -Escreva 8 GigaByteParaMegaByte \n -Escreva 9 GigaByteParaTeraByte \n -Escreva 10 TeraByteParaGigaByte \n - Escreva 11 TeraByteParaPetaByte \n -Escreva 12 PetaByteParaTeraByte')
funcEscolha = input()

if(funcEscolha =='1'):
    entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
    valorConvertido = BitParaByte(entradaDoTecladoValorASerConvertido)
    print(valorConvertido)

if(funcEscolha =='2'):
    entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
    valorConvertido = ByteParaBit(entradaDoTecladoValorASerConvertido)
    print(valorConvertido)

if(funcEscolha =='3'):
    entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
    valorConvertido = ByteParaKiloByte(entradaDoTecladoValorASerConvertido)
    print(valorConvertido)

if(funcEscolha =='4'):
    entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
    valorConvertido = KilobyteParaByte(entradaDoTecladoValorASerConvertido)
    print(valorConvertido)

if(funcEscolha =='5'):
    entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
    valorConvertido = KiloByteParaMegaByte(entradaDoTecladoValorASerConvertido)
    print(valorConvertido)

if(funcEscolha =='6'):
    entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
    valorConvertido = MegaByteParaKiloByte(entradaDoTecladoValorASerConvertido)
    print(valorConvertido)

if(funcEscolha =='7'):
    entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
    valorConvertido = MegaByteParaGigaByte(entradaDoTecladoValorASerConvertido)
    print(valorConvertido)

if(funcEscolha =='8'):
    entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
    valorConvertido = GigaByteParaMegaByte(entradaDoTecladoValorASerConvertido)
    print(valorConvertido)

if(funcEscolha =='9'):
    entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
    valorConvertido = GigaByteParaTeraByte(entradaDoTecladoValorASerConvertido)
    print(valorConvertido)

if(funcEscolha =='10'):
    entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
    valorConvertido = TeraByteParaGigaByte(entradaDoTecladoValorASerConvertido)
    print(valorConvertido)

if(funcEscolha =='11'):
    entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
    valorConvertido = TeraByteParaPetaByte(entradaDoTecladoValorASerConvertido)
    print(valorConvertido)

if(funcEscolha =='12'):
    entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
    valorConvertido = PetaByteParaTeraByte(entradaDoTecladoValorASerConvertido)
    print(valorConvertido)

    