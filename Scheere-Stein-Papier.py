import random, sys

def willkommen():
    print('''
Willkommen! Viel Spaß mit Schere-Stein-Papier
Regeln:
Schere schlägt Papier
Papier schlägt Stein
Stein schlägt Schere
-Sofie Preißinger
''')

willkommen()

num_rounds = int(input('Geben Sie die Anzahl der Runden ein die Sie spielen möchten: '))





def schereSteinPapierSpiel(num_rounds):

    print ('Schere-Stein-Papier')

gewonnen = 0
verloren = 0
unentschieden = 0

for _ in range(num_rounds):
    print ('%s gewonnen, %s verloren, %s unentschieden' % (gewonnen, verloren, unentschieden))

    while True :
        print ('Bitte Option wählen: Schere(1) Stein(2) Papier(3) oder (b)eenden')
        playerMove = input()

        if playerMove == 'b':
                sys.exit()
        if playerMove == '1' or playerMove == '2' or playerMove == '3':
                break
        print ('Bitte 1,2,3 oder b eingeben')



    if playerMove == '1':
        print ('SCHERE gegen ...')
    elif playerMove == '2':
        print ('STEIN gegen ...')
    elif playerMove == '3':
        print ('PAPIER gegen ...')



    randomNumber = random.randint(1, 3)

    if randomNumber == 1:
        computerMove = '1'
        print ('SCHERE')
    elif randomNumber == 2:
        computerMove = '2'
        print ('STEIN')
    elif randomNumber == 3:
        computerMove = '3'
        print ('PAPIER')



    if playerMove == computerMove :
        print ('es ist unentschieden!')
        unentschieden = unentschieden + 1

    elif playerMove =='2' and computerMove =='1':
        print ('Sie haben gewonnen!')
        gewonnen = gewonnen + 1
    elif playerMove == '3' and computerMove == '2':
        print ('Sie haben gewonnen!')
        gewonnen = gewonnen + 1
    elif playerMove == '1' and computerMove == '3':
        print('Sie haben gewonnen!')
        gewonnen = gewonnen + 1

    else :
        print ('Sie haben leider verloren')
        verloren = verloren + 1

print ('Spiel beendet!')
print ('%s gewonnene Runden, %s verlorene Runden, %s unentschiedene Runden' % (gewonnen, verloren, unentschieden))



