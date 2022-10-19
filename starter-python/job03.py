# j'ai déclarez une variable “âge”, qui prendra la valeur saisie par l’utilisateur.
age = int(input("Bonjour, quel âge as tu ?"))
# j'ai fait en sorte que si lage est inferieur a 18 ca affichera "tu es mineur"
if age < 18:
     print("Tu es mineur")
# j'ai fait en sorte que si lage est inferieur a 18 ca affichera "tu es majeur"
elif age >= 18:
     print("Tu es majeur")