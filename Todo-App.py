print("Todo Liste\n" )

tasks=[] #[]=Leere Liste

def aufgabe_hinzufuegen(aufgabe):
    tasks.append(aufgabe) #append=Eine Methode zur Liste"tasks" hinzufuegen

def zeige_aufgaben():
    for i,t in enumerate(tasks,1):  #Nummerierung beginnt bei 1
        print(f"{i}.{t}") #f=f-string, mit{} Variable einsetzen, t=Aufgabe, i=Nummer

while True:
    print("1: Aufgabe hinzufuegen, 2: Aufgaben anzeigen, 3. Beenden")
    auswahl=input("Bitte wählen")
    if auswahl == "1":
       aufgabe_hinzufuegen(input("Aufgabe eingeben: "))
    elif auswahl == "2":
         zeige_aufgaben()
    elif auswahl == "3":
         break
    else:
         print("Ungültige Auswahl")
