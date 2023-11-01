#FORCA



def forca(palavra):
    erro = 0   
    fases = [" ",
              "____     ",
              "|        ",
              "|   |    ",
              "|   0    ",
              "|  /|\   ",
              "|  / \   ",
              "|        ",
              ]
    letras_restantes = list(palavra)
    painel = ["__"] * len(palavra)
    vitoria = False
    print("WELCOME TO HANGMAN!!!")
    
    while erro < len(fases) - 1:
        print("\n")
        msg = "Guess a letter: "
        caractere = input(msg)
        
        if caractere in letras_restantes:
            indice_atual = letras_restantes.index(caractere)
            painel[indice_atual] = caractere
            letras_restantes[indice_atual] = '$'
        else:
            erro += 1
        print((" ".join(painel)))
        e = erro + 1
        print("\n".join(fases[0:e]))
        if "__" not in painel:
            print("Você ganhou!")
            print(" ".join(painel))
            vitoria = True
            break
    if not vitoria:
        print("\n".join(fases[0:erro]))
        print("Você perdeu! A palavra era {}.".format(palavra))

forca("consistency")
    
    
    
            
