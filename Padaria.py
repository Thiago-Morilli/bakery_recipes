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
        print("\n Opcao invalida!")
        self.Voltar_menu()


    def texto(self):
        linha = '*' * (90)  
        print(linha)
      
       
       
    def Pao_normal(self):
        self.texto()
        usuario = float(input("Qual é a quantidade de massa: "))
        self.texto()

        farinha = usuario          


        farinha_centeio = farinha * 100 / 1.000
        fermento = farinha * 40 / 1.000
        sal = farinha * 20 / 1.000
        produto = farinha * 1.1 / 1000
        agua = farinha * 0.750 / 1.000

        print(f"\nPara {farinha:.0f}kg de farinha vai: ")
        print(f"{farinha_centeio}kg de farinha de centeio")
        print(f"{sal}kg de sal")
        print(f"{produto}kg  de produto")
        print(f"{fermento}kg de fermento")
        print (f"{agua}l de agua")

        while True:
            self.texto()
            usuario_02 = str(input("Voce quer saber para que essa massa serve? [S/N] ")).upper()
            self.texto()

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
        self.texto()
        usuario = int(input("Qual é a quantidade de massa: "))
        self.texto()
        

        produto = usuario
      
        agua = produto * 0.450 / 1.000
        fermento = produto * 80 / 1.000
 
        print(f"Para {produto:.0f}kg de produto vai: ")
        print(f"{agua:.3f}l de agua")
        print(f"{fermento:.0f}kg de fermento")
        print("Lembre-se de fazer 30 croissant pro dia aseguir")

        while True:
            self.texto()
            usuario_02 = str(input("Voce quer saber para que essa massa serve? [S/N] ")).upper()
            self.texto()

            if usuario_02 == "S":
                print({"Lancheiras": ["Fiambre E Queijo (Quantidade: 3)",
                "Fiambre E Chorico (quantidade: 3)",
                "pizzas (Quantidade : 3)"
                ]})
                self.Voltar_menu()

            elif usuario_02 == "N":
                print("Obrigado") 
                self.Voltar_menu()
      


    def massa_bolas(self):
        self.texto()
        usuario = float(input("\nQual é a quantidade de massa: "))
        self.texto()
        
        farinha = usuario

        sal = farinha * 20 /  1.000
        produto = farinha * 10 / 1.000
        azeite = farinha * 100 / 1.000
        fermento = farinha * 40 / 1.000
        ovos = farinha * 6 / 1.000
        agua = "olho"
        produto_amarelo = "Um pouco"
 
        print(f"Para {farinha:.0f}kg de farinha vai: ")
        print(f"{produto:.0f}kg de produto")
        print(f"{sal}kg de sal")
        print(f"{ovos:.0f} ovos")
        print(f"{fermento}kg de fermento")
        print(f"Agua: {agua}")
        print(f"{azeite}ml de azeite")
        print(f"Produto Amarelo: {produto_amarelo}")
        print("Pesar bolas com: 300kg")

        while True:
            self.texto()
            usuario_02 = str(input("\nVoce quer saber para que essa massa serve? [S/N] "))
            self.texto()
       
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
        self.texto()
        usuario = int(input("\nQual é a quantidade de massa: "))
        self.texto()

        farinha = usuario
        leite = farinha * 500 / 1.000
        produto = farinha * 25 / 1.000
        acucar = farinha * 200 / 1.000
        fermento = farinha * 150 / 1.000
        sal = farinha * 25 / 1.000
        ovos = farinha * 2 / 1.000

        print(f"\nPara {farinha}kg de farinha")
        print(f"{produto}kg de produto")
        print(f"{acucar}kg de acucar")
        print(f"{sal}kg de sal")
        print(f"{fermento}kg de fermento")
        print(f"{ovos} ovos")
        print(f"{leite}l de leite")

        print("\nPintar com ovos e colocar sementes.")


    def biscoitos(self):
        self.texto()
        usuario = int(input("\nQual é a quantidade de massa: "))
        self.texto()

        farinha = usuario
        acucar = farinha * 500 / 1.000
        ovos = farinha * 6 / 1.000
        fermento_po = farinha * 2 / 1.000
        bicarbonato = farinha * 2 / 1.000
                                                   

        print(f"{farinha}kg farinha vai :")
        print(f"{acucar}kg de acucar")
        print(f"{ovos} ovos")
        print(f"{fermento_po} colheres de fermento em po")
        print(f"{bicarbonato} colheres de bicarconato")
        print("Um pouco de azeite")
        print("Um pouco de leite")


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
