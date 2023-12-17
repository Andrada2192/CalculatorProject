class CalculatorSimplu:

    def __init__(self, valoare_initiala=0.0):
        self.valoare_curenta = float(valoare_initiala)

    def adunare(self, numar):
        self.valoare_curenta += numar

    def scadere(self, numar):
        self.valoare_curenta -= numar

    def inmultire(self, numar):
        self.valoare_curenta *= numar

    def impartire(self, numar):
        if numar != 0:
            self.valoare_curenta /= numar
        else:
            print('Nu se poate face impartirea')

    def valoare_start(self, numar):
        self.valoare_curenta = numar        #val curenta, adica cea de start este 0.0, deci o sa fie egala cu prima valoare pe care utilizatorul o sa o introduca in consola

    def afisare_valoare_curenta(self):
        print(self.valoare_curenta)

calculator = CalculatorSimplu()


def afisare_rezultat():
    print(calculator.valoare_curenta)

    while True:
        date_utilizator = input('> ')
        operatii = date_utilizator

        if operatii == 'x' or operatii == 'X':      #utilizatorul poate folosi atat 'x' cat si 'X' pentru a incheia programul
            calculator.afisare_valoare_curenta()
            print('Iesire din program')
            break

        operatie = operatii[0]

        try:
            numar = float(operatii[1:])
        except (ValueError, IndexError):
            print('Operatie invalida')
            continue

        if operatie == '+':
            calculator.adunare(numar)
        elif operatie == '-':
            calculator.scadere(numar)
        elif operatie == '*':
            calculator.inmultire(numar)
        elif operatie == '/':
            calculator.impartire(numar)
        else:
            print('Sunt acceptate doar operatiile: +, -, *, /, x sau X')

        calculator.afisare_valoare_curenta()