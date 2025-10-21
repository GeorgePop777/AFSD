
text = """România a înregistrat o creștere semnificativă a numărului de turiști în acest an, 
conform datelor publicate de Institutul Național de Statistică. 
Cele mai populare destinații rămân Brașov, Cluj-Napoca și București."""

mijloc = len(text) // 2
prima_parte = text[:mijloc]
a_doua_parte = text[mijloc:]

prima_parte = prima_parte.upper()
prima_parte = prima_parte.strip()

a_doua_parte = a_doua_parte[::-1]
a_doua_parte = a_doua_parte.capitalize()
for punct in ".,!?":
    a_doua_parte = a_doua_parte.replace(punct, "")

rezultat = prima_parte + a_doua_parte
print("Rezultatul final este:\n")
print(rezultat)