from verden import Verden

def hovedprogram():
    verden = Verden(int(input('Oppgi antall rader : ')), int((input('Oppgi antall kolonner : '))))
    verden.tegn()
    input_m = input('Press \'Enter\'-tasten for å fortsette, eller, Tast inn \'q\' for å avslutte :')
    while input_m != 'q':
        if input_m == '':
            verden.oppdatering()
            verden.tegn()
        else:
            print('Ugyldig input, prøv på nytt!\n')
        input_m = input('Press \'Enter\'-tasten for å fortsette. Tast inn \'q\' for å avslutte :')


# starte hovedprogrammet
hovedprogram()