elevi = ["Ana", "Bogdan", "Carmen", "Darius", "Elena"]
note  = [9,       7,        10,       4,        8]

elev_nou        = "Felix"
nota_elev_nou   = 6
elev_de_sters   = "Darius"

interogari_nume = ["Ana", "Mara", "Elena", "stop"]

absente = [1, 0, 2, 3, 0]

####notele elevilor######

for i in range(len(elevi)):  ##len=lungimea liste si range=secventa de numere de la 0 la len si i=variabila a buclei###
    print(f"{elevi[i]} are nota {note[i]}") ###f=foloseste str direct dintre ghilimele###
print()

####notele maxime si minime#######

nota_max = max(note)
nota_min = min(note)
elevi_max = [elevi[i] for i in range(len(elevi)) if note[i] == nota_max]
elevi_min = [elevi[i] for i in range(len(elevi)) if note[i] == nota_min]

print(f"Nota maximă este {nota_max}, obținută de: {', '.join(elevi_max)}") ###join=uneste caracterele dintro lista intrun singur sir#####
print(f"Nota minimă este {nota_min}, obținută de: {', '.join(elevi_min)}\n")

###media clasei###

media = sum(note) / len(note)
print(f"Media clasei este: {media:.2f}\n") ##.2f=variabila pentru 2 zecimale si \n=linie noua####

####promovati####

for i in range(len(elevi)):
    if note[i] >= 5:
        print(f"{elevi[i]} {note[i]}")
print()

###+1 la nota####

for i in range(len(note)):
    note[i] = min(note[i] + 1, 10) ###min=compara rezultatul cu 10 si ia valoarea cea mai mica####
print("Notele după creștere cu 1 punct (max 10):", note, "\n")

###adaugam elev nou###

elevi.append(elev_nou)
note.append(nota_elev_nou)
print("După adăugarea elevului nou:")
print("Elevi:", elevi)
print("Note:", note, "\n")

###stergere elev predefinit###

if elev_de_sters in elevi:
    poz=elevi.index(elev_de_sters)
    del elevi[poz]
    del note[poz]
    print(f"Elevul {elev_de_sters} a fost șters.\n")

###afisarea din nou a listei###

for i in range(len(elevi)):
    print(f"{elevi[i]} are nota {note[i]}")

####cautari de statistici##

i = 0 #index de 0#
while i < len(interogari_nume) and interogari_nume[i] != "stop": #daca apare stop#
    nume = interogari_nume[i]
    if nume in elevi:
        poz = elevi.index(nume)
        print(f"{nume} are nota {note[poz]}")
    else:
        print(f"{nume} nu există în listă.")
    i += 1

###număr promovați / respinși###

promovati = sum(1 for n in note if n >= 5)
respinsi = len(note) - promovati
print(f"Promovați: {promovati}, Respinși: {respinsi}\n")

###media promovatilor###

note_promovati = [n for n in note if n >= 5]
if note_promovati:
    media_promovati = sum(note_promovati) / len(note_promovati)
    print(f"Media promovaților este: {media_promovati:.2f}")
else:
    print("Nu există elevi promovați.")