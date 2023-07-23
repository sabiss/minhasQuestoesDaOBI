palavraParaCifrar = input()

alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'z']
vogais = ['a','e','i','o','u']
consoantes = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'x', 'z']

novaPalavra = ""

for letra in palavraParaCifrar:
    if letra in consoantes:
        novaPalavra+=letra#guardo a consoante original
        posicaoDaLetraNoAlfabeto = alfabeto.index(letra)#qual a posicao daquela consoante no alfabeto
        letraParaDireita = 0
        letraParaEsquerda = 0
        distanciaDaConsoanteParaDireita = 0
        distanciaDaConsoanteParaEsquerda = 0

        for i in range(posicaoDaLetraNoAlfabeto+1, len(alfabeto), +1):#indo pra direita
            #vou procurando qual é a próxima vogal
            distanciaDaConsoanteParaDireita+=1#marca a distância daquela vogal até a consoante original
            if alfabeto[i] in vogais:
                letraParaDireita = vogais[vogais.index(alfabeto[i])]
                break

        for e in range(posicaoDaLetraNoAlfabeto-1, 0, -1):#indo pra esquerda
            #for e in range(partida, parada, operação)
            distanciaDaConsoanteParaEsquerda+=1
            if alfabeto[e] in vogais:
                letraParaEsquerda = vogais[vogais.index(alfabeto[e])]
                break
        indexLetraPraDireita = alfabeto.index(letraParaDireita)
        indexLetraPraEsquerda = alfabeto.index(letraParaEsquerda)

        if distanciaDaConsoanteParaDireita == distanciaDaConsoanteParaEsquerda:
            novaPalavra+=letraParaEsquerda
        elif distanciaDaConsoanteParaDireita < distanciaDaConsoanteParaEsquerda:
            novaPalavra+=letraParaDireita
        else:
            novaPalavra+=letraParaEsquerda
        for a in range (posicaoDaLetraNoAlfabeto+1, len(alfabeto), +1):
            if alfabeto[a] in consoantes:
                novaPalavra+=alfabeto[a]
                break
    else:
        novaPalavra+=letra
print(novaPalavra)

                

            

