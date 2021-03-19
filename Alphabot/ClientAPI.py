import requests 
from AlphaBot import AlphaBot
from Sensori import * 
from Infrared_Obstacle_Avoidance import * 

Ab = AlphaBot()

def menuPercorsi():
    URL = "http://127.0.0.1:5000/api/v1/resources/luoghi/all"
    res = requests.get(url = URL)
    luoghi = res.json()
    #print(luoghi["1"])

    URL2 = "http://127.0.0.1:5000/api/v1/resources/inizio_fine/all"
    res2 = requests.get(url = URL2)
    percorso = res2.json()

    print("Percorsi che puoi fare: ")
    for i in percorso: 
        idstart, idend = percorso[str(i)]
        print(luoghi[str(idstart)][0] + " -> " + luoghi[str(idend)][0])

    inizio = input("Inserisci l'aula di partenza: ")
    fine = input("Inserisci l'aula di arrivo: ")

    URL3 = "http://127.0.0.1:5000/api/v1/resources/inizio_fine"
    param = {'start': inizio, 'end': fine}
    res3 = requests.get(url = URL3, params = param)
    return res3.json()

def main():
    percorso = menuPercorsi()
    comandi, valori = convertString(percorso)
    print(comandi)
    print(valori)
    for i in range(0, len(comandi)):
        gestioneOstacoli(comandi[i], valori[i], Ab)
if __name__ == "__main__":
    main()