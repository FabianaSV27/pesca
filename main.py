import random

class jogoPesca:

    def __init__(self):
        self.possiveis_peixe = ['Baiacu', 'Atum', 'Lambari', 'Sardinha', 'Namorado', 'Tilapia', 'Pintado', 'Tubarao', 'Betta', 'Pacu', 'Pirarucu']
        self.peixe_pescado = None

    def pesca(self, peixe_escolhido):
        self.peixe_pescado = random.choice(self.possiveis_peixe)

    def iniciar_jogo(self):
        print("Bem-vindo à Pescaria! Escolha o peixe que quer pescar:")
        print(f"Nossos peixes são: {self.possiveis_peixe}")

        peixe_escolhido = input("Escolha seu Peixe:")

        self.pesca(peixe_escolhido)

        print(""" 
                   /|
                  / |
                 /  |
                /   |
               /    ¿
              /
             /
            / """)

        if self.peixe_pescado:
            print(f"Você pescou um {self.peixe_pescado}")

            print("""  
                       /|
                      / |
                     /  |
                    /   |
                   /    ¿
                  /      🐟
                 /
                / """)

        if self.peixe_pescado == peixe_escolhido:
            print("Parabéns, você pescou o peixe que escolheu!")
        else:
            print("Infelizmente não foi o peixe que escolheu :( Tente novamente!")

jogo = jogoPesca()
jogo.iniciar_jogo()
