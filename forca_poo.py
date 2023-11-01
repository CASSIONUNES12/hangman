class Forca:
    fases = [" ",
              "____     ",
              "|        ",
              "|   |    ",
              "|   0    ",
              "|  /|\   ",
              "|  / \   ",
              "|        ",
              ]
    
    def __init__(self,palavra):
        self.palavra = palavra
        self.painel = ['__'] * len(palavra)
        self.erros = 0
        self.letras_restantes = list(palavra)

    def mostrar_painel(self):
        print(" ".join(self.painel))

    def exibir_forca(self):
        e = self.erros + 1
        print("\n".join(self.fases[0:e]))

    def jogar(self):
        print("BEM-VINDO AO JOGO DA FORCA!\n")
        while self.erros < len(self.fases):
            
            resposta = input("Tente adivinhar a palavra; digite uma letra: ").lower()

            if len(resposta) != 1 or not resposta.isalpha():
                print("Por favor, digite apenas uma letra.")
                continue
            
            if resposta in self.letras_restantes:
                in_atual = self.letras_restantes.index(resposta)
                self.painel[in_atual] = resposta
                self.letras_restantes[in_atual] = '$'
                self.mostrar_painel()
            else:
                self.erros += 1
                self.exibir_forca()
                self.derrota()
            
            if "__" not in self.painel:
                print("Você ganhou!")
                print(" ".join(self.painel))
                break
    
    
    def derrota(self):
            if self.erros >= len(self.fases):
                print("Você perdeu. A palavra era {}".format(self.palavra))
        
           
jogo = Forca("gato")
jogo.jogar()
