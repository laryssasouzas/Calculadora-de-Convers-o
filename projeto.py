padrão = 1024

def converterStringParaFloat(value):
    print('Valor convertido de str para float')
    return float(value)

def BitParaByte(valorASerConvertido):
    print('Valor convertido de Bit para Byte')
    ByteCalculado = valorASerConvertido / 8
    return ByteCalculado

def ByteParaBit(valorASerConvertido):
    print('Valor convertido de Byte para Bit')
    BitCalculado = valorASerConvertido * 8
    return BitCalculado

def ByteParaKiloByte(valorASerConvertido):
    print('Valor convertido de Byte para KiloByte')
    KiloByteCalculado = valorASerConvertido / padrão
    return KiloByteCalculado

def KilobyteParaByte(valorASerConvertido):
    print('Valor convertido de KiloByte para Byte')
    ByteCalculado = valorASerConvertido * padrão
    return ByteCalculado

def KiloByteParaMegaByte(valorASerConvertido):
    print('Valor convertido de KiloByte para MegaByte')
    MegaByteCalculado = valorASerConvertido / padrão
    return MegaByteCalculado

def MegaByteParaKiloByte(valorASerConvertido):
    print('Valor convertido de MegaByte para KiloByte')
    KiloByteCalculado = valorASerConvertido * padrão
    return KiloByteCalculado

def MegaByteParaGigaByte(valorASerConvertido):
    print('Valor convertido de MegaByte para GigaByte')
    GigaByteCalculado = valorASerConvertido / padrão
    return GigaByteCalculado

def GigaByteParaMegaByte(valorASerConvertido):
    print('Valor convertido de GigaByte para MegaByte')
    MegaByteCalculado = valorASerConvertido * padrão
    return MegaByteCalculado

def GigaByteParaTeraByte(valorASerConvertido):
    print('Valor convertido de GigaByte para TeraByte')
    TeraByteCalculado = valorASerConvertido / padrão
    return TeraByteCalculado

def TeraByteParaGigaByte(valorASerConvertido):
    print('Valor convertido de TeraByte para GigaByte')
    GigaByteCalculado = valorASerConvertido * padrão
    return GigaByteCalculado

def TeraByteParaPetaByte(valorASerConvertido):
    print('Valor convertido de TeraByte para PetaByte')
    PetaBytesCalculado = valorASerConvertido / padrão
    return PetaBytesCalculado

def PetaByteParaTeraByte(valorASerConvertido):
    print('Valor convertido de PetaByte para TeraByte')
    TeraByteCalculado = valorASerConvertido * padrão
    return TeraByteCalculado

print('Insira o valor a ser convertido')
ValorInicial = converterStringParaFloat(input())
valorConvertido = TeraByteParaPetaByte(ValorInicial)
print(valorConvertido)