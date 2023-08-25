from rutenett import Rutenett


class Verden:
    def __init__(self, rader, kolonner):
        self._rutenett = Rutenett(rader, kolonner)
        self._generasjonsnummer = 0
        self._rutenett.fyll_med_tilfeldige_celler()
        self._rutenett.koble_celler()

    def tegn(self):
        self._rutenett.tegn_rutenett()
        print('Generasjons Nummer : {}\nAntall Levende Celler : {}\n'.format(self._generasjonsnummer,
                                                                             self._rutenett.antall_levende()))

    def oppdatering(self):
        alle_celler = self._rutenett.hent_alle_celler()
        for celle in alle_celler:
            celle.tell_levende_naboer()
        for celle in alle_celler:
            celle.oppdater_status()
        self._generasjonsnummer += 1
