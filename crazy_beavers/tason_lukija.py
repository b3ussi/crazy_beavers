import pathlib
from perus_palikka import PALIKAN_KOKO

def lue_taso(taso_tiedosto: pathlib.Path):
    with open(taso_tiedosto, 'r') as f:
        lines = f.read().splitlines()

    return lines


class Kartta:
    def __init__(self, tiedosto: pathlib.Path):
        self.tiedosto = pathlib.Path(tiedosto)
        if not self.tiedosto.exists():
            raise RuntimeError(f"Tiedostoa {self.tiedosto} ei ole olemassa")

        with open(self.tiedosto, 'r') as f:
            self.data = f.read().splitlines()

        self.pituus = len(self.data[0]) * PALIKAN_KOKO
        self.korkeus = len(self.data) * PALIKAN_KOKO