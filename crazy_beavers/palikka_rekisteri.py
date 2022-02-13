from perus_palikka import Palikka
_PALIKKA_REKISTERI = {}

def rekisteroi_palikka(palikka: Palikka):
    _PALIKKA_REKISTERI[palikka.symboli] = palikka
    print(f"rekisteröity palikka {palikka.__name__}")
    
def hae_palikka(symboli: str):
    if symboli not in _PALIKKA_REKISTERI:
        raise RuntimeError(f"Palikkaa ei ole rekisteröity symbolille {symboli}")
    
    return _PALIKKA_REKISTERI[symboli]