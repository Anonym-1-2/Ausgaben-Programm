"""
 1. while schleife für abfrage
 2. user input mit den ausgaben speichern
 3. die ausgaben addiert ausgeben
 4. den User sectionen erstellen lassen
 5. das der user entscheiden kann zu welche section die Ausgabe reingehört
 6. die ausgaben sections weise abgeben oder als ganzes abgeben
"""

import json


try:
    with open("datenbank.json", "r") as datei:
       user_listen  = json.load(datei)
except FileNotFoundError:
    user_listen = {} 



def erstellung():
            benennen = input("Wie soll die Section heissen?: ")
            user_listen[benennen] = []
            print(f"Section '{benennen}' wurde erstellt.")
            try:
                ausgaben_input = float(input(f"Wie viele Franken Ausgaben soll ich in die Section {benennen} hinzufügen?: "))
                user_listen[benennen].append(ausgaben_input)
            except ValueError:
                  print("Bitte nur Zahlen eingeben, danke.")
                  del user_listen[benennen]

def anzeige():
            for name, werte in user_listen.items():
                total = sum(werte)
                print(f"{name}: {total:.2f} Franken")


def hinzufügung():
                     
            werte_hinzufügen_suche = input("Zu welcher section möchtest du Abzüge hinzufügen?: ")
            for name, werte in user_listen.items():
                if werte_hinzufügen_suche in name:
                    try:
                        werte_hinzufügen = float(input("Wieviel Franken abzüge möchtest du hinzufügen?: "))
                        user_listen[werte_hinzufügen_suche].append(werte_hinzufügen)
                    except ValueError:
                          print("Bitte nur Zahlen eingeben, danke.")
                          
                else:
                    continue

def löschen():
      
      keys_löschen = input("Welche Section möchtest du löschen?: ")
      if keys_löschen in user_listen:
            zustimmung = input(f"Möchtest du {keys_löschen} wirklich löschen?(y/n): ").upper()
            if zustimmung in ["Y", "YES","JA", "J"]:
                  del user_listen[keys_löschen]
                  print(f"{keys_löschen} wurde gelöscht.")
            



while True:
     stamm_input = input("Welche Funktion möchtest du anwenden?(erstellen(1), anzeigen(2), hinzufügen(3), löschen(4), beenden/speichern(5)): ").upper()

     if stamm_input in ["ERSTELLEN","ERSTELLUNG", "ERSTELL", "1"] :
          erstellung()
     elif stamm_input in ["ANZEIGEN", "ZEIGEAN", "ANZEIGE", "2"]:
          anzeige()
     elif stamm_input in ["HINZUFÜGEN", "HINZUFÜGUNG", "3"]:
          hinzufügung()
     elif stamm_input in ["LÖSCHEN", "LÖSCH", "4"]:
          löschen()
     else:
          print("Das Programm wird beendet und gespeichert.")
          break
     


with open("datenbank.json", "w") as datei:
    json.dump(user_listen, datei)

  
  

          
       

