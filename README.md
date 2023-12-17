# MiniCalculator Project PY


Se dorește implementarea unei aplicații de tip mini - calculator în mod text în Python. La pornire aplicația afișează valoarea inițială care este
implicit 0. Valoarea inițială se poate seta prin intermediul unui parametru din linia de comanda. Apoi aplicația așteaptă o operație de la utilizator și
afișează rezultatul acestuia.

#### Operațiile posibile sunt:
  - +număr - adună la valoarea curentă numărul respectiv
  - -număr - scade din valoarea curentă numărul respectiv
  - *număr - înmulțește valoarea curentă numărul respectiv
  - /număr - împarte valoarea curentă la numărul respectiv
  - =număr - setează valoarea curentă cu numărul respectiv
  - x - ieșire din program

După fiecare operație se va afișa valoarea curentă și se așteaptă din nou un input de la utilizator. Linia pe care se așteaptă input-ul de la utilizator
începe cu semnul "> ".
Dacă o comandă nu poate fi înțeleasă sau executată, se va afișa mesajul "Invalid operation"

#### Structura proiect => principii OOP (clase și obiecte). 

Am creat un Python Package, calculators care contine 3 fisiere python:
  - _ _init_ _.py 
  - calculator_simplu.py => in acest fisier am creat clasa CalculatorSimplu() și metodele necesare pentru operațiile aritmetice (+, -, *, /) precum si metoda de afișare a rezultatului
  - main.py(fisierul unde se ruleaza aplicatia) => aici am importat clasa CalculatorSimplu() prin comanda: from calculators.calculator_simplu import CalculatorSimplu, precum si functia afisare_rezultat() prin comanda: from calculators.calculator_simplu import afisare_rezultat si am creat obiectul calculator

  


