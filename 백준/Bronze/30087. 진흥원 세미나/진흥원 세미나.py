n = int(input())
list = ["Algorithm","DataAnalysis","ArtificialIntelligence","CyberSecurity","Network","Startup","TestStrategy"]
number = ["204","207","302","B101","303","501","105"]
for i in range(n):
    semina = input()
    for ii in range(0,7):
        if semina == list[ii]:
            print(number[ii])