# Crazy Beaver
 
## Pelin idea

- Pelin tavoitteena edetä tasolta toiselle
- Beaver Clan koostuu majavista, jotka taistelevat majavamiestä vastaan
- Majavien kanssa samalla puolella on Jooseppi, joka on luonnosuojelia sekä velho
- Majavat aloittavat matkansa aina aloituspisteestä → Kun majavat ovat lähteneet liikeelle, niiden perään lähtee majava-mies, 
  joka jahtaa majavia tason loppuun saakka. Jos tasoa ei suorita tarpeeksi nopeassa ajassa, majava-mies saa majavan kiinni ja 
  tason häviää. Tason aikana vastaan tulee erilaisia esteitä eli majavan pitää osata hypätä, ryömiä, liikkua eteenpäin ja 
  taakseppäin sekä jyrsiä vastaan tulevia puita
 - Ensimmäisillä tasoilla majavana toimii Gunilla, sitten Xenia ja vaikeimmilla eli viimeisillä tasoilla majavaklaanin johtajamajava Masa. Kun peli on läpäisty loppuun voisi ilmestyä video, jossa Jooseppi ja majavat juhlivat ja majavamies viedään selliin. Taso alkaa kun yksi majavista (riippuen tasosta) lähtee pakenemaan majavamiestä. Tason aikana vastaan tulee esteitä, jotka majavan tulee ohittaa tarpeeksi nopeassa ajassa, jotta majavmies ei saa kiinni. Kun majava on suorittanut tasoin viimeisen esteen, se pääsee padolle (luonnonsuojelualuetta), jossa sitä odottaa Jooseppi. Jooseppi estää rehtinä luonnonsuojelijana majavamiehen pääsyn padolle, ja näin taso on suoritettu ja eteen tulee valikko kaikista läpäistyistä tasoista, joista vain ennestään pelatut ovat auki ja muiden päällä on lukko, eli pelaaja tulee läpäistä aikaisempi taso, jos mielii päästä seuraavalle tasolle. Jokainen taso aikaisempaa vaikeampi ja pelin viimeisillä tasoilla pitää olla hyvät refleksit & lihasmuisti. Jokaisella tasolla on erilainen maailma/ymäristö joita voisivat olla esim saha, asuinalue ja kuusimetsä. Pelissä on ainakin kolme sydäntä ja jos ne menettää, pelaaja joutuu aloittamaan ensimmäiseltä tasolta (välissä voi olla jonkinlaisia checkpointeja, ettei tarvitse aina aloittaa nollasta)   




## Grafiikka

## Hahmot

####Jooseppi
Luonnonsuojelija sekä velho, jonka luokse tason suorittaneet majavat menevät. Jooseppi on NPC, eikä se ole tasoissa mukana muulloin kun taso on suoritettu. Jooseppi liikkuu hitaasti
####Majavat
Majavia ovat Xenia, Masa sekä Gunilla. Majavat kuuluvat majavaklaaniin. Majavien tehtävänä on kulkea kentän/tason läpi, eli alkupisteestä padolle. Ne ovat siis pelaajan liikuteltavissa. Pelaaja liikuttaa aina vain yhtä majavaa kerrallaan (Ainakin ensimmäisllä tasoilla). Majavien liike kosstuu kahdesta "kuvasta" (kuvien erot jalkojen sekä hännän asennossa. Jyrsiessä majavan hampaat tulevat näkyviin). Majavien liikettä on juokseminen, jyrsiminen ja uiminen. 
####Death
Death on NPC ja se ilmestyy vain jos majava ei suorita tasoa. Death:n liike siten, että kun majava kuolee, sen päälle ilmestyy hautakivi, josta nousee ylös Death. Tähän kuluu max. 4 sekuntia. 
####Majavamies
Majavamies jahtaa majavia jokaisessa tasossa. Mitä pidemälle tasoissa edetään, sitä nopeammin majavamies liikkuu. Majavamies on NPC. Se liikkuu kaikkien esteiden yli tai ali ja sen vauhti on läpi tason tasaista. Majavamies lähtee majavien perään joitakin sekunteja myöhemmin kuin majavat. Kun elämät loppuvat, eli majavamies on ottamut majvat kiinni niin monta kertaa kun sydämmiä on, ilmestyy video, jossa majavamies myy majavahattuja/turkkeja torilla virne kasvoillaan

### NPC (eipelaajahahmot)

Sellaiset tyypit jotka liikkuu, mutta eivät ole pelaajan hallittavissa. Esim majavamies
* NPC:tä ovat majavamies, Jooseppi ja Death


### Staattiset oliot

Kaikki sellaiset asiat jotka vaikuttavat hahmojen liikkumiseen, mutta jotka eivät aktiivisesti liiku 

* Puut: Puita generoituu taustalle ain epäsäännöllisin aikavälein. Puita ei voi ohittaa, eli ne ovat vain tasutalla. Puut voivat erilaisia (määrittyy tason tyylin mukaan. Esim. aavikolla ei voi kasvaa mäntyjä)
* Kivet: Kivien yli voi hypätä. Harmaita möykkyjä, jotka ovat etenkin alkutasoilla yleisiä.
* Vesialue/suo: Vesi alueen yli tulee uida ja jos sitä ei ui, liikkuu todella hitaasti. Ovat aika harvinaisia, eli eivät ilmesty kuin max. muutamia kertoja per. taso
* Kaatunut puunrunko: Majava pystyy jyrsimään itsensä puunrungon läpi. Puunrungot ovat kohtalaisen yleisiä ja ne generoituvat niin päin, että vuosirenkaat näkyvät 
* Kolo: Kolojen läpi majavat ryömivät. Ne ovat mustanvärisiä aukkoja, jotka ovat kooltaan pieniä. Kolojen päällä on maata
* kanto: Puiden kantoja. Vain yhden lajin kantoja (eli ei esim. koivun ja kuusen kantoja). Kantojen yli voi hypätä samalla tavalla kuin kivien

## Ohjelmointi

## Pelimoottori

## Linkit

## Maailma

##Kontrollit
* D=eteenpäin
* A=taaksepäin
* shift=ryömi 
 * E=jyrsi
* space=hyppää
* esc=mainmenu
* ctrl=ui (jos majava ei ui, se liiikku vedessä paljon hitaammin)
* enter/left m = kun haluaa aloittaa uuden tason pelaamisen (click to play)
 * Mah. lisäys: Tuplahyppy?



##Tulevaisuutta varten:
Hahmo-luokat
1. Majavat. Toiminnallisuus oikeaksi. Majava-luokka saadaan näyttämään miltä halutaan (ei vielä välttämättä visuaalisesti)



