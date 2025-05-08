titoli = []
n = int(input("Quanti titoli vuoi inserire: "))
for i in range(n):
    titolo = input("Inserisci un titolo di un articolo: ")
    titoli.append(titolo)

parole_sospette = {
    "scoperta segreta": -2,
    "sconvolgente": -1,
    "esclusivo": -1,
    "il governo nasconde": -2,
    "nessuno ne parla": -1,
    "teoria del complotto": -2,
    "emergenza": -1,
    "urgenza": -1,
    "incredibile": -1,
    "mai visto prima": -1
}

parole_rassicuranti = {
    "studio scientifico": +2,
    "ricerca": +1,
    "testimoniato": +1,
    "verificato": +2,
    "fatti concreti": +2,
    "approvato": +1,
    "fonti ufficiali": +2,
    "esito positivo": +1,
    "verificato da esperti": +2,
    "dati confermati": +2
}

def analizza_titolo(titolo):
    titolo = titolo.lower() 
    punteggio = 0  

    for parola, valore in parole_sospette.items():
        if parola in titolo:
            punteggio += valore 

    for parola, valore in parole_rassicuranti.items():
        if parola in titolo:
            punteggio += valore 

    return punteggio

def visualizza_classifica(titoli):
    risultati = []
    numero = 1  

    for titolo in titoli:
        punteggio = analizza_titolo(titolo)
        risultati.append((titolo, punteggio))  

    print("Classifica delle notizie:")
    for titolo, punteggio in risultati:
        
        classificazione = (
            "Fake news" if punteggio < -3 else
            "Notizia affidabile" if punteggio > 3 else
            "Notizia dubbia"
        )
        print(f"{numero}. {titolo} - Punteggio: {punteggio} - Classificazione: {classificazione}")
        numero += 1 

visualizza_classifica(titoli)
