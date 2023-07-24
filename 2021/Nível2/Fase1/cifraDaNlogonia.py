palavraParaCifrar = input()

alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'z']
vogais = ['a','e','i','o','u']
consoantes = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'x', 'z']

novaPalavra = ""

for letra in palavraParaCifrar:
    if letra in consoantes:
        novaPalavra+=letra#guardo a consoante original
        posicaoDaLetraNoAlfabeto = alfabeto.index(letra)#qual a posicao daquela consoante no alfabeto
        vogalParaDireita = 0
        vogalParaEsquerda = 0
        distanciaDaConsoanteParaDireita = 0
        distanciaDaConsoanteParaEsquerda = 0
        if letra != 'z':
            for i in range(posicaoDaLetraNoAlfabeto+1, len(alfabeto), +1):#indo pra direita
                #vou procurando qual é a próxima vogal
                distanciaDaConsoanteParaDireita+=1#marca a distância daquela vogal até a consoante original
                if alfabeto[i] in vogais:#achando a próxima vogal da consoante
                    vogalParaDireita = vogais[vogais.index(alfabeto[i])]
                    break
        for e in range(posicaoDaLetraNoAlfabeto-1, -1, -1):#indo pra esquerda
            #for e in range(partida, parada, operação)
            distanciaDaConsoanteParaEsquerda+=1
            if alfabeto[e] in vogais:
                vogalParaEsquerda = vogais[vogais.index(alfabeto[e])]
                break
        if letra != 'z':
            if vogalParaDireita != 0:#se tiver vogal para direita
                if distanciaDaConsoanteParaDireita == distanciaDaConsoanteParaEsquerda:
                    novaPalavra+=vogalParaEsquerda
                elif distanciaDaConsoanteParaDireita < distanciaDaConsoanteParaEsquerda:
                    novaPalavra+=vogalParaDireita
                else:
                    novaPalavra+=vogalParaEsquerda
            else:#não teve vogal para direita
                novaPalavra+=vogalParaEsquerda

            for a in range (posicaoDaLetraNoAlfabeto+1, len(alfabeto), +1):#próxima consoante
                if letra == 'z':
                    novaPalavra+= "z"
                    break
                else:
                    if alfabeto[a] in consoantes:
                        novaPalavra+=alfabeto[a]
                        break
        else:#se a letra for Z não vai ter mais nenhuma letra pra direita então a vogal deve ser a da esquerda
            novaPalavra+=vogalParaEsquerda
            novaPalavra+="z"#sua próxima consoante deve ser obrigatoriamente Z
    else:
        novaPalavra+=letra
print(novaPalavra)