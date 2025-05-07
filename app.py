titoli = []
n = int(input("quanti titoli vuoi inserire: "))
for i in range(n):
    titolo = input("inserisci un titolo di un articolo: ")
    titoli.append(titolo)

# Parole sospette con punteggi personalizzati
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

# Parole rassicuranti con punteggi personalizzati
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
            punteggio += valore  # somma punteggio negativo

    for parola, valore in parole_rassicuranti.items():
        if parola in titolo:
            punteggio += valore  # somma punteggio positivo

    return punteggio

def visualizza_classifica(titoli):
    risultati = []
    for titolo in titoli:
        punteggio = analizza_titolo(titolo)
        risultati.append((titolo, punteggio))

    # Ordina in base al punteggio, dal più alto al più basso
    risultati.sort(key=lambda x: x[1], reverse=True)

    print("Classifica delle notizie:")
    for count, (titolo, punteggio) in enumerate(risultati, start=1):
        classificazione = (
            "Fake news" if punteggio < -3 else
            "Notizia affidabile" if punteggio > 3 else
            "Notizia dubbia"
        )
        print(f"{count}. {titolo} - Punteggio: {punteggio} - Classificazione: {classificazione}")

# Analizza e stampa
print(analizza_titolo(titolo))
visualizza_classifica(titoli)
