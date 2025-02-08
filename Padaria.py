import os
# Fazer outra class com outras receitas

class Receitas:

    def title(self):
        texto = "RECEITAS DA PADARIA"
        print(texto.center(50))
        

    def exibir_opcoes(self):
        print("1. Pao Normal")
        print("2. Croissant")
        print("3. Massa De Bolas")
        print("4. pao de cachorro")
        print("5. biscoitos")


    def Voltar_menu(self):
        input('\nDigite uma tecla para voltar ao menu: ')
        self.main()


    def opcao_invalida(self):
        self.texto("\n Opcao invalida!")
        self.Voltar_menu()


    def texto(self,texto):
        linha = '*' * (len(texto))
        print(texto)
        
       
    def Pao_normal(self):
        
        usuario = float(input("\nQual é a quantidade de massa: "))

        farinha = usuario          


        farinha_centeio = farinha * 100 / 1.000
        fermento = farinha * 40 / 1.000
        sal = farinha * 20 / 1.000
        produto = farinha * 1.1 / 1000
        agua = farinha * 0.750 / 1.000

        self.texto(f"\nPara {farinha:.0f}kg de farinha vai: ")
        self.texto(f"{farinha_centeio}kg de farinha de centeio")
        self.texto(f"{sal}kg de sal")
        self.texto(f"{produto}kg  de produto")
        self.texto(f"{agua}ml de agua")

        while True:
            usuario_02 = str(input("\nVoce quer saber para que essa massa serve? [S/N] "))
            print()

            if usuario_02 == "S":
                print("Serve para: ",
                ["4 Baguetes Pequenas",
                 "2 Baguetes Grandes",
                  "6 Pao De Chorico (preparo: 1 pao e meio)",
                   "2 Bola Da Vo: 350kg", "10 Broas: 600kg",
                    "Bifanas: 3,750kg"
                    ])
                self.Voltar_menu()

            elif usuario_02 == "N":
                print("Obrigado") 
                self.Voltar_menu()
            
        
    def Croissant(self):
        usuario = int(input("Qual é a quantidade de massa: "))
        print()

        produto = usuario
      
        agua = produto * 0.450 / 1.000
        fermento = produto * 80 / 1.000
 
        self.texto(f"Para {produto:.0f}kg de produto vai: ")
        self.texto(f"{agua:.3f}ml de agua")
        self.texto(f"{fermento:.0f}kg de fermento")
        print("Lembre-se de fazer 30 croissant pro dia aseguir")

        while True:
            usuario_02 = str(input("Voce quer saber para que essa massa serve? [S/N] "))

            if usuario_02 == "S":
                print({"Lancheiras": ["Fiambre E Queijo (Quantidade: 3)",
                "Fiambre E Chorico (quantidade: 3)",
                "pizzas (Quantidade : 3)"
                ]})
                self.Voltar_menu()

            elif usuario_02 == "N":
                print("Obrigado") 
                self.Voltar_menu()
        print()


    def massa_bolas(self):
        usuario = float(input("\nQual é a quantidade de massa: "))
        print()

        farinha = usuario

        sal = farinha * 20 /  1.000
        produto = farinha * 10 / 1.000
        azeite = farinha * 100 / 1.000
        fermento = farinha * 40 / 1.000
        ovos = farinha * 6 / 1.000
        agua = "olho"
        produto_amarelo = "Um pouco"
 
        self.texto(f"Para {farinha:.0f}kg de farinha vai: ")
        self.texto(f"{produto:.0f}kg de produto")
        self.texto(f"{sal}kg de sal")
        self.texto(f"{ovos:.0f} ovos")
        self.texto(f"{fermento}kg de fermento")
        self.texto(f"Agua: {agua}")
        self.texto(f"{azeite}ml de azeite")
        self.texto(f"Produto Amarelo: {produto_amarelo}")
        print("Pesar bolas com: 300kg")

        while True:
            usuario_02 = str(input("\nVoce quer saber para que essa massa serve? [S/N] "))
            print()
       
            if usuario_02 == "S":
                print({"Serve para": ["Bolas de carne",
                 "bolas de azeite",
                  "filhosas (obs: tem que cortar)",
                   "fulares (4 por dia)",
                    "Pao amarelo (pesar com: 600kg e quantidade: 5 )"
                ]})
                self.Voltar_menu()

            elif usuario_02 == "N":
                print("Obrigado") 
                self.Voltar_menu()


    def pao_de_cachorro(self):

        usuario = int(input("\nQual é a quantidade de massa: "))

        farinha = usuario
        leite = farinha * 500 / 1.000
        produto = farinha * 25 / 1.000
        acucar = farinha * 200 / 1.000
        fermento = farinha * 150 / 1.000
        sal = farinha * 25 / 1.000
        ovos = farinha * 2 / 1.000

        self.texto(f"\nPara {farinha}kg de farinha")
        self.texto(f"{produto}kg de produto")
        self.texto(f"{acucar}kg de acucar")
        self.texto(f"{sal}kg de sal")
        self.texto(f"{fermento}kg de fermento")
        self.texto(f"{ovos} ovos")
        self.texto(f"{leite}l de leite")

        print("\nPintar com ovos e colocar sementes.")


    def biscoitos(self):
        usuario = int(input("\nQual é a quantidade de massa: "))

        farinha = usuario
        acucar = farinha * 500 / 1.000
        ovos = farinha * 6 / 1.000
        fermento_po = farinha * 2 / 1.000
        bicarbonato = farinha * 2 / 1.000
                                                   

        self.texto(f"\n{farinha}kg farinha vai :")
        self.texto(f"{acucar}kg de acucar")
        self.texto(f"{ovos} ovos")
        self.texto(f"{fermento_po} colheres de fermento em po")
        self.texto(f"{bicarbonato} colheres de bicarconato")
        self.texto("Um pouco de azeite")
        self.texto("Um pouco de leite")


    def escolher_opcao(self):
        try:
            opcao_escolhida = int(input('Escolha uma opção: '))
    
            if opcao_escolhida == 1: 
                self.Pao_normal()
            elif opcao_escolhida == 2: 
                self.Croissant()
            elif opcao_escolhida == 3:
                self.massa_bolas()
            elif opcao_escolhida == 4:
                self.pao_de_cachorro()
            elif opcao_escolhida == 5:
                self.biscoitos()
            else:
                self.opcao_invalida()
        except:
            self.opcao_invalida()
        

    def main(self):
        os.system('clear')
        self.title()
        self.exibir_opcoes()
        self. escolher_opcao()
        
Receitas().main()
