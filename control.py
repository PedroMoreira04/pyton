from exercicios import Exercicios


def exercicios():
    pass


class Menu:
    def __init__(self):
        self.opcao = -1
        self.exer  = exercicios()
        self.num1  = 0
        self.num2  = 0
        self.num3 = 0
        self.total = 0
        self.imposto = 0
        self.porc = 0
        self.fabrica = 0



    def mostrarMenu(self):
        print('\n ----MENU----\n\n'             +
              'Escolha uma das opções abaixo: ' +
              '\n0. Sair'                       +
              '\n1. Somar'                      +
              '\n2. Subtrair'                   +
              '\n3. Dividir'                    +
              '\n4. Multiplicar'                +
              '\n5. Potência'                   +
              '\n6. raiz'                       +
              '\n7. Tabuada'                    +
              '\n8. exercicio 1'                +
              '\n9  exercicio 2'                +
              '\n10 exercicio 3'                +
              '\n11 exercicio 4'                +
              '\n12 exercicio 5'                +
              '\n13 exercicio 6'                +
              '\n14 exercicio 7'                +
              '\n15 exercicio 8'                +
              '\n16 exercicio 9'                +
              '\n17 exercicio 10'               +
              '\n18 exercicio 11'               +
              '\n19 exercicio 12'               +
              '\n20 exercicio 13'               +
              '\n21 exercicio 14'               +
              '\n22 exercicio 15'               +
              '\n23 exercicio 16'               +
              '\n24 exercicio 17'               +
              '\n25 exercicio 18'               +
              '\n26 exercicio 19'               +
              '\n27 exercicio 20'               +
              '\n\n----- LISTA 2 -----\n' +
              '\n28 exercicio 21'               +
              '\n29 exercicio 22'               +
              '\n30 exercicio 23'               +
              '\n31 exercicio 24'               +
              '\n32 exercicio 25'               +
              '\n33 exercicio 26'               +
              '\n34 exercicio 27'               +
              '\n35 exercicio 28'               +
              '\n36 exercicio 29')

    def coletar(self):
        self.num1 = int(input("Informe o primeiro número: "))
        self.num2 = int(input("Informe o segundo número: "))
        self.math = ("")

    def control(self):
        while self.opcao != 0:
            self.mostrarMenu()  # Chamando as opções
            self.opcao = int(input('Escolha uma das opções acima:'))
            if self.opcao == 0:
                print('Obrigado!')
            elif self.opcao == 1:
                self.coletar()#Chamando o  input por meio do coletar
                print(f'A soma dos números digitados é: {self.exer.somar(self.num1,self.num2)}')
            elif self.opcao == 2:
                self.coletar()
                print(f'A subtração dos números digitados é: {self.exer.subtrair(self.num1, self.num2)}')
            elif self.opcao == 3:
                self.coletar()
                print(f'A multiplicação dos números digitados é: {self.exer.multiplicar(self.num1, self.num2)}')
            elif self.opcao == 4:
                self.coletar()
                print(f'A divisão dos números digitados é: {self.exer.dividir(self.num1, self.num2)}')
            elif self.opcao == 5:
                self.coletar()
                print(f'A potência dos números digitados é: {self.exer.potencia(self.num1, self.num2)}')
            elif self.opcao == 6:
                self.coletar()  # Chamando o input
                print(f'A raiz de {self.num1} é: {self.exer.raiz(self.num1)}')
                print(f'A raiz de {self.num2} é: {self.exer.raiz(self.num2)}')
            elif self.opcao == 7:
                self.coletar()  # Chamando o input
                print(f'A tabuada do {self.num1} é: {self.exer.tabuada(self.num1)}')
                print(f'A tabuada do {self.num2} é: {self.exer.tabuada(self.num2)}')
            elif(self.opcao == 8):
                print(self.exer.exercicio1())
            elif(self.opcao == 9):
                print(self.exer.exercicio2())
            elif (self.opcao == 10):
                print(self.exer.exercicio3())
            elif (self.opcao == 11):
                print(self.exer.exercicio4())
            elif (self.opcao == 12):
                print(self.exer.exercicio5(self.num1))
            elif (self.opcao == 13):
                print(self.exer.exercicio6(self.num1))
            elif (self.opcao == 14):
                print(self.exer.exercicio7(self.num1))
            elif (self.opcao == 15):
                print(self.exer.exercicio8(self.num1))
            elif (self.opcao == 16):
                print(self.exer.exercicio9(self.num1))
            elif (self.opcao == 17):
                print(self.exer.exercicio10(self.num1))
            elif (self.opcao == 18):
                print(self.exer.exercicio11(self.num1))
            elif (self.opcao == 19):
                print(self.exer.exercicio12(self.num1))
            elif (self.opcao == 20):
                print(self.exer.exercicio13(self.num1))
            elif (self.opcao == 21):
                print(self.exer.exercicio14(self.num1))
            elif (self.opcao == 22):
                print(self.exer.exercicio15(self.num1))
            elif (self.opcao == 23):
                print(self.exer.exercicio16(self.num1))
            elif (self.opcao == 24):
                print(self.exer.exercicio17())
            elif (self.opcao == 25):
                print(self.exer.exercicio18())
            elif (self.opcao == 26):
                print(self.exer.exercicio19())
            elif (self.opcao == 27):
                print(self.exer.exercicio20(self.num1))
            elif (self.opcao == 28):
                print(self.exer.exercicio21(self.num1))
            elif (self.opcao == 29):
                print(self.exer.exercicio22(self.num1))
            elif (self.opcao == 30):
                print(self.exer.exercicio23(self.num1))
            elif (self.opcao == 31):
                print(self.exer.exercicio24(self.num1))
            elif (self.opcao == 32):
                print(self.exer.exercicio25(self.num1))
            elif (self.opcao == 33):
                print(self.exer.exercicio26(self.num1))
            elif (self.opcao == 34):
                print(self.exer.exercicio27(self.total))
                print(self.exer.exercicio27(self.fabrica))
                print(self.exer.exercicio27(self.imposto))
                print(self.exer.exercicio27(self.porc))

            elif (self.opcao == 35):
                int(input("Informe a Primeira nota:"))
                int(input("Informe a Segunda nota:"))
                int(input("Informe a Terceira nota:"))
                print(f'A tabuada do {self.num1} é: {self.exer.exercicio28(self.num1)}')
                print(f'A tabuada do {self.num2} é: {self.exer.exercicio28(self.num2)}')
                print(f'A tabuada do {self.num3} é: {self.exer.exercicio28(self.num3)}')










            else:
                print("Codigo escolhido não é valído!")