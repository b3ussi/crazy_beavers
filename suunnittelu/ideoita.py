class Hahmo:
    def __init__(self):
        self.liike_lista = []
        self.lue_kuvat('c:\Users\Otto\majava_kuvat')
        self.liike_indeksi = 0
        self.paikka = 0

    def lue_kuvat(self, kuva_tiedostot):
        for kuva_tiedosto in kuva_tiedostot:
            kuva = image_read(kuva_tiedosto)
            self.liike_lista.append(kuva)

    def liiku(self):
        self.animoi(self.liike_lista[self.liike_indeksi])
        self.liike_indeksi = self.liike_indeksi + 1
        self.paikka = self.paikka + 10.4


class Jooseppi:
    pass


class MajavaMies:
    pass


class Majava:
    pass


class StaattinenJuttu:

    def __init__(self):
        self.kuka_voi_syoda = []

    def voi_syoda(self, kuka):
        return kuka in self.kuka_voi_syoda

    def syo_minut(self, kuka):
        pass

    def tormaa(self):
        self._pida_aanta(self.tormays_aani)


class Puu(StaattinenJuttu):
    def __init__(self):
        self.kuka_voi_syoda = [Majava]
        self.tormays_aani = 'kops.mp4'
        self.syomis_aani = 'rouskis.mp4'

    def syo_minut(self, kuka):
        self._pida_aanta(self.syomis_aani)


class Kivi(StaattinenJuttu):
    def __init__(self):
        self.tormays_aani = 'bang.mp4'
        self.kuka_voi_syoda = None


class Latakko(StaattinenJuttu):
    def __init__(self):
        self.tormays_aani = 'loiskis.mp4'