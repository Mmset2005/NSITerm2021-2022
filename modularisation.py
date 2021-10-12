from notes import*
# Script du programme : Série de notes

# demander à l’utilisateur combien de notes il souhaite saisir → [ n ]
nb_notes = demander_entier_V2("Combien de notes sont à saisir ? ")

# saisir les [ n ] notes comprise entre [ 0 ; 20 ]
notes = [ saisir_note() for i in range(nb_notes)]

# afficher la note la plus faible et la note la plus élevée
print(f"La note mini est {minimum_table(notes)}")
print(f"La note maxi est {maximum_table(notes)}")

# calculer la moyenne
print(f"La moyenne des notes est {moyenne_table(notes)}")