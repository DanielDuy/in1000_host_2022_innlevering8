from random import randint
from celle import Celle


class Rutenett:
    def __init__(self, rader, kolonner):
        self._ant_rader = rader
        self._ant_kolonner = kolonner
        self._rutenett = self._lag_tomt_rutenett()

    def _lag_tomt_rutenett(self):
        rute = []
        for a in range(self._ant_rader):
            rute.append(self._lag_tom_rad())
        return rute

    def _lag_tom_rad(self):
        liste = []
        for a in range(self._ant_kolonner):
            liste.append(None)
        return liste

    def fyll_med_tilfeldige_celler(self):
        for r in range(self._ant_rader):
            for k in range(self._ant_kolonner):
                self.lag_celle(r, k)

    def lag_celle(self, rad, kol):
        ny_celle = Celle()
        if randint(0, 2) == 0:
            ny_celle.sett_levende()
        self._rutenett[rad][kol] = ny_celle

    def hent_celle(self, rad, kol):
        if (0 <= rad < self._ant_rader) and (0 <= kol < self._ant_kolonner):
            return self._rutenett[rad][kol]
        return None

    def tegn_rutenett(self):
        for rad in self._rutenett:
            for celle in rad:
                print(celle.hent_status_tegn(), end=' ')
            print('')

    def _sett_naboer(self, rad, kol):
        celle = self.hent_celle(rad, kol)
        pr_r = [rad-1, rad, rad+1]
        pr_k = [kol-1, kol, kol+1]

        for r in pr_r:
            for k in pr_k:
                temp_celle = self.hent_celle(r, k)
                if temp_celle is not None and not(rad == r and kol == k):
                    celle.legg_til_nabo(temp_celle)

    def koble_celler(self):
        for r in range(self._ant_rader):
            for k in range(self._ant_kolonner):
                self._sett_naboer(r, k)

    def hent_alle_celler(self):
        alle_celler = [celle for rad in self._rutenett for celle in rad]
        return alle_celler

    def antall_levende(self):
        celler = self.hent_alle_celler()
        levende = 0
        for celle in celler:
            if celle.hent_status_tegn() == 'O':
                levende += 1
        return levende
